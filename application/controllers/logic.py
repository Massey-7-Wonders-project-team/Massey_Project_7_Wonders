from ..models.card import Card
from ..models.player import Player
from ..models.game import Game
from ..models.cardhist import Cardhist
from ..models.round import Round
from ..models.wonder import Wonder
from index import db
import random


def deal_wonders(players):
    wonders = Wonder.query.all()

    for player in players:
        wonder = wonders.pop(random.randint(0, len(wonders)-1))
        player.wonder = wonder.name

        card = Card.query.filter_by(name=wonder.card_0).first()
        update_player(card, player)
        db.session.add(player)

    try:
        db.session.commit()
    except Exception as e:
        print(e)


def deal_hands(age, players):
    """Call to have the next age's hands dealt"""
    cards = Card.query.filter(Card.noPlayers <= len(players)).filter_by(age=age).all()

    try:
        # Randomly assign cards to players
        for player in players:
            for j in range(7):
                param = random.randint(0, len(cards)-1)
                card = cards.pop(param)
                dealt_card = Round(age=age, round=1, playerId=player.id, cardId=card.id)
                db.session.add(dealt_card)
        db.session.commit()
    except Exception as e:
        print(e)


def set_neighbours(players):
    """Called at the beginning of the game to set player's left_id and right_id"""
    num_players = len(players)
    i = num_players

    try:
        for player in players:
            player.left_id = players[(i-1) % num_players].id
            player.right_id = players[(i+1) % num_players].id
            db.session.add(player)
            i += 1

        db.session.commit()
    except Exception as e:
        print(e)


def check_move(card, player):
    """Call before processing card to check that it is a valid move, returns boolean"""

    if (card.costStone > player.stone or
        card.costBrick > player.brick or
        card.costOre > player.ore or
        card.costWood > player.wood or
        card.costGlass > player.glass or
        card.costPaper > player.paper or
        card.costCloth > player.cloth or
        card.costMoney > player.money):
        return False
    else:
        return True


def update_player(card, player, for_wonder=False):
    """Helper function for process_card"""
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

    try:
        db.session.add(game_info)
        db.session.commit()
    except Exception as e:
        print(e)


def update_db(card, player, is_discarded, for_wonder, game_info):
    old_round = Round.query.filter_by(playerId=player.id, age=game_info.age, round=game_info.round).first()
    old_round.remove(card)

    if game_info.age == 2:
        next_player = player.right_id
    else:
        next_player = player.left_id

    try:
        db.session.add(player)

        history = Cardhist(playerId=player.id, cardId=card.id, discarded=is_discarded, for_wonder=for_wonder)
        db.session.add(history)

        for unplayed_card in old_round:
            next_round = Round(playerId=next_player, age=game_info.age, round=game_info.round + 1,
                               cardId=unplayed_card.id)
            db.session.add(next_round)

        db.session.commit()
    except Exception as e:
        print(e)


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
