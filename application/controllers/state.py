from ..models.card import Card
from ..models.player import Player
from flask import jsonify

def print_json (player, cards):
    return {
        'player': player.serialise(),
        'cards': [card.serialise() for card in cards]
    }
