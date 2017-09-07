from ..models.card import Card
from ..models.player import Player
from ..models.game import Game
from ..models.cardhist import Cardhist
from ..models.round import Round
from ..models.wonder import Wonder
from index import db
import copy
import random


def deal_wonders(players):
    wonders = Wonder.query.all()

    cardhists = []

    for player in players:
        wonder = wonders.pop(random.randint(0, len(wonders)-1))
        player.wonder = wonder.name

        card = Card.query.filter_by(name=wonder.card_0).first()
        update_player(card, player)
        cardhists.append(Cardhist(playerId=player.id, cardId=card.id, discarded=False, for_wonder=True))

    db_add(p=players, c=cardhists)


def deal_hands(age, players):
    """Call to have the next age's hands dealt"""
    cards = Card.query.filter(Card.noPlayers <= len(players)).filter_by(age=age).all()

    # Randomly assign cards to players
    dealt_cards = []
    for player in players:
        for j in range(7):
            param = random.randint(0, len(cards)-1)
            card = cards.pop(param)
            dealt_cards.append(Round(age=age, round=1, playerId=player.id, cardId=card.id))

    db_add(d=dealt_cards)


def set_neighbours(players):
    """Called at the beginning of the game to set player's left_id and right_id"""
    num_players = len(players)
    i = num_players

    for player in players:
        player.left_id = players[(i-1) % num_players].id
        player.right_id = players[(i+1) % num_players].id
        i += 1

    db_add(p=players)


def check_move(card, player):
    """Call before processing card to check that it is a valid move, returns boolean"""

    # Checks if card can be played using prerequisites
    if (card.prerequisite1 is not None
        and Card.query.filter_by(name=card.prerequisite1).join(Cardhist).filter_by(playerId=player.id) is not None
        or card.prerequisite2 is not None
        and Card.query.filter_by(name=card.prerequisite2).join(Cardhist).filter_by(playerId=player.id) is not None):
        return True

    # Check money
    if card.costMoney > player.money:
        return False

    balance = [card.costStone - player.stone, card.costBrick - player.brick, card.costOre - player.ore,
               card.costWood - player.wood, card.costGlass - player.glass, card.costPaper - player.paper,
               card.costCloth - player.cloth]

    # If true, there are materials missing, and checks for resource alternating materials ensues
    if filter(lambda x: x > 0, balance) is not None:
        extra = [player.extra_stone, player.extra_brick, player.extra_ore, player.extra_wood, player.extra_glass,
                 player.extra_paper, player.extra_cloth]
        maximum = [x-y for (x,y) in zip(balance, extra)]

        # Investigates if there is a permutation that will work after checking that there could be a chance of success
        if filter(lambda x: x > 0, maximum) is not None:
            return False
        else:
            ra_cards = (Cardhist.query.filter_by(playerId=player.id, discarded=False).join(Card)
                        .filter_by(resourceAlternating=True)
                        .with_entities(Card.giveStone, Card.giveBrick, Card.giveOre, Card.giveWood,
                                       Card.giveGlass, Card.givePaper, Card.giveCloth)).all()

            return rec_search(balance, ra_cards)

    # Triggers if there are enough materials without considering resource alternation
    else:
        return True


def rec_search(balance, cards):
    """Helper function for check_move. Checks resource permutations for alternating resource cards
     Returns False if not possible, True if possible"""
    if filter(lambda x: x > 0, balance) is None:
        return True
    if cards is None:
        return False

    new_cards = copy.deepcopy(cards)
    new_bal = copy.deepcopy(balance)

    for card in new_cards:
        c = new_cards.pop(card)

        for i in range(len(balance)):
            if balance[i] > 0 and c[i] > 0:
                new_bal[i] -= c[i]
                if rec_search(new_bal, new_cards):
                    return True
                else:
                    # Roll back changes from iteration
                    new_bal[i] += c[i]

    # Search sub-space exhausted without success
    return False


def update_player(card, player, for_wonder=False):
    """Helper function for process_card"""
    if card.resourceAlternating is True:
        player.extra_brick += card.giveBrick
        player.extra_ore += card.giveOre
        player.extra_wood += card.giveWood
        player.extra_stone += card.giveStone
        player.extra_paper += card.givePaper
        player.extra_cloth += card.giveCloth
        player.extra_glass += card.giveGlass
    else:
        player.brick += card.giveBrick
        player.ore += card.giveOre
        player.wood += card.giveWood
        player.stone += card.giveStone
        player.paper += card.givePaper
        player.cloth += card.giveCloth
        player.glass += card.giveGlass
        player.military += card.giveMilitary
        player.money += card.giveMoney - card.costMoney
        player.points += card.givePoints

    if for_wonder:
        player.wonder_level += 1


def set_next_round(game_info, players):
    """Helper function to process_card, changes round"""
    game_info.round += 1

    if game_info.round == 7:
        game_info.round = 1
        game_info.age += 1
        if game_info.age == 4:
            game_info.complete = True
            # TODO FINAL CALCULATIONS FOR END GAME
        else:
            deal_hands(game_info.age, players)

    db_add(game=game_info)


def update_db(card, player, is_discarded, for_wonder, game_info):

    old_round_cardId = db.session.query(Round.cardId).filter_by(playerId=player.id, age=game_info.age, round=game_info.round).all()
    old_round_list = [i[0] for i in old_round_cardId]

    old_round_list.remove(card.id)

    if game_info.age == 2:
        next_player = player.right_id
    else:
        next_player = player.left_id

    history = Cardhist(playerId=player.id, cardId=card.id, discarded=is_discarded, for_wonder=for_wonder)

    rounds = []
    for unplayed_card in old_round_list:
        rounds.append(Round(playerId=next_player, age=game_info.age, round=game_info.round + 1,
                            cardId=unplayed_card))

    db_add(p=player, h=history, r=rounds)


def find_wonder_card(player):
    """Logic for processing a turn where a wonder is built"""
    wonder = Wonder.query.filter_by(id=player.wonder).first()

    # Makes sure a wonder is not played when it is already maxed out
    if wonder.slots is player.wonder_level:
        return False

    # Finds wonder card and returns it
    if player.wonder_level == 1:
        card = Card.query.filter_by(id=wonder.card_1).first()
    elif player.wonder_level == 2:
        card = Card.query.filter_by(id=wonder.card_2).first()
    elif player.wonder_level == 3:
        card = Card.query.filter_by(id=wonder.card_3).first()
    else:
        card = Card.query.filter_by(id=wonder.card_4).first()

    return card


def process_card(card, player, is_discarded, for_wonder):
    """Called from play_card API endpoint, plays card, updates DB, and checks if able to go to next turn
    Returns false if card unable to be played, otherwise true"""
    if is_discarded:
        player.money += 3
    else:
        if for_wonder:
            # use wonder card instead of played card
            card = find_wonder_card(player)
        if card is False or check_move(card, player) is False:
            return False
        update_player(card, player, for_wonder)

    # UPDATE DB
    game_info = Game.query.filter_by(id=player.gameId).first()
    update_db(card, player, is_discarded, for_wonder, game_info)

    # TURN COMPLETION LOGIC
    players = (Player.query.filter_by(gameId=player.gameId)).all()
    for p in players:
        if Round.query.filter_by(age=game_info.age, round=game_info.round+1, playerId=p.id) is None:
            return True

    # Only triggers if all players have finished their turn
    set_next_round(game_info, players)
    return True


def db_add(*args, **kwargs):
    try:
        for value in args:
            print('args')
            db.session.add_all(value)
        for key, value in kwargs.items():
            if type(value) is list:
               db.session.add_all(value)
            else:
               db.session.add(value)
        db.session.commit()
    except Exception as e:
        print('Error commiting database update')
        print(e)
