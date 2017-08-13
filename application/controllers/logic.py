from ..models.card import Card
from ..models.player import Player
from ..models.game import Game
from ..models.cardhist import Cardhist
from ..models.round import Round
from index import db
import random


def deal_hands(age, players):
    cards = Card.query.filter_by(Card.noPlayers <= len(players)).filter_by(age=age).all()
    print("Number of cards drawn are: " + len(cards))

    for player in players:
        for j in range(7):
            card = cards.pop(random.len(cards))
            dealt_card = round(age=age, round=1, playerId=player.id, cardId=card.id)
            db.add(dealt_card)
    db.commit_all()

"""
def check_move (card, player, is_discarded, for_wonder):

    if is_discarded:
        return True

    if for_wonder:
        # check if wonder requirements are met

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
"""

def process_card(card, player, is_discarded, for_wonder):
    # checks move is valid, returns false if not
    #if not check_move(card, player, is_discarded, for_wonder):
    #    return False
    if is_discarded:
        player.money += 3

        history = Cardhist(playerId=player.id, cardId=card.id, discarded=True)
        db.add(history)

    else:
        if card.colour == 'brown':
            player.brick += card.giveBrick
            player.ore += card.giveOre
            player.wood += card.giveWood
            player.stone += card.giveStone
        if card.colour == 'grey':
            player.paper += card.givePaper
            player.cloth += card.giveCloth
            player.glass += card.giveGlass
        if card.colour == 'red':
            player.military += card.giveMilitary
        player.money += card.giveMoney - card.costMoney
        player.points += card.givePoints

        history = Cardhist(playerId=player.id, cardId=card.id, discarded=False)
        db.add(history)


    #############
    # Update DB #
    #############
    game_info = Game.query.filter_by(id=player.gameId).first()
    old_round = (Round.query
                 .filter_by(playerId=player.id)
                 .filter_by(age=game_info.age)
                 .filter_by(round=game_info.round)).first()

    age = game_info.age
    round_number = game_info.round
    old_round.remove(card)

    if age == 2:
        next_player = player.right_id
    else:
        next_player = player.left_id

    for unplayed in old_round:
        next_round = round(playerId=next_player, age=age, round=round_number+1, cardId=unplayed.id)
        db.add(next_round)

    db.add(player)
    db.commit_all()


    #########################
    # TURN COMPLETION LOGIC #
    #########################
    players = (Player.query.filter_by(gameId=player.gameId)).all()
    for p in players:
        if Round.query.filter_by(age=age, round=round_number+1, playerId=p.id) is None:
            return

    # Only triggers if all players have finished their turn
    game_info.round += 1
    if game_info.round == 7:
        game_info.round = 1
        game_info.age += 1
        if game_info.age == 4:
            game_info.complete = True
            # TODO FINAL CALCULATIONS FOR END GAME
        else:
            deal_hands(game_info.age, players)

    db.add(game_info)
    db.commit_all()
