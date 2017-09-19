from ..models.card import Card
from ..models.player import Player
from flask import jsonify


def print_json (player, players, cards):
    """print({
        'player': player.serialise(),
        'allPlayers': [player.serialise() for player in players],
        'cards': [card.serialise() for card in cards],
    })"""
    return {
        'player': player.serialise(),
        'allPlayers': [p.serialise() for p in players if p is not player],
        'cards': [card.serialise() for card in cards],
    }


def false_true (string):
    if string == 'false':
        return False
    elif string == 'true':
        return True
    print(string + " given into false_true function")