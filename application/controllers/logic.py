from ..models.card import Card
from ..models.player import Player
from ..models.game import Game
from ..models.cardhist import Cardhist
from ..models.round import Round
from index import db
import random


def deal_hands(age, players):
    """Call to have the next age's hands dealt"""
    if (age not in range(1, 4)) or (len(players) not in range(3, 8)):
        print("Invalid call, age: " + age + " Number of players: " + len(players))
        return False

    cards = Card.query.filter(Card.noPlayers <= len(players)).filter_by(age=age).all()
    if len(cards) is not 7*len(players):
        print("Incorrect number of cards in age: " + age + " Number of players: " + len(players))
        return False

    try:
        # Randomly assign cards to players
        for player in players:
            for j in range(7):
                param = random.randint(0, len(cards)-1)
                card = cards.pop(param)
                dealt_card = Round(age=age, roundNum=1, playerId=player.id, cardId=card.id)
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
    except Error as e:
        print(e)


def check_move(card, player, is_discarded, for_wonder):
    """Call before processing card to check that it is a valid move, returns boolean"""
    if is_discarded:
        return True

    if for_wonder:
        pass
        # TODO IMPLEMENT WONDER LOGIC

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


def update_player(card, player):
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


def update_db(card, player, is_discarded, game_info):
    old_round = Round.query.filter_by(playerId=player.id, age=game_info.age, round=game_info.round).first()
    old_round.remove(card)

    if game_info.age == 2:
        next_player = player.right_id
    else:
        next_player = player.left_id

    try:
        db.session.add(player)

        history = Cardhist(playerId=player.id, cardId=card.id, discarded=is_discarded)
        db.session.add(history)

        for unplayed_card in old_round:
            next_round = Round(playerId=next_player, age=game_info.age, round=game_info.round + 1,
                               cardId=unplayed_card.id)
            db.session.add(next_round)

        db.session.commit()
    except Exception as e:
        print(e)


def process_card(card, player, is_discarded, for_wonder):
    """Called from play_card API endpoint, plays card, updates DB, and checks if able to go to next turn
    Returns false if card unable to be played, otherwise true"""
    if not check_move(card, player, is_discarded, for_wonder):
        return False

    # UPDATE PLAYER
    if is_discarded:
        player.money += 3
    elif for_wonder:
        pass
        # TODO WONDER LOGIC
    else:
        update_player(card, player)

    # UPDATE DB
    game_info = Game.query.filter_by(id=player.gameId).first()
    update_db(card, player, is_discarded, game_info)

    # TURN COMPLETION LOGIC
    players = (Player.query.filter_by(gameId=player.gameId)).all()
    for p in players:
        if Round.query.filter_by(age=game_info.age, round=game_info.round+1, playerId=p.id) is None:
            return True

    # Only triggers if all players have finished their turn
    set_next_round(game_info, players)
    return True
