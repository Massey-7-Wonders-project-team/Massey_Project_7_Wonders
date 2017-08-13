from ..models.card import Card
from ..models.player import Player
from flask import jsonify

class State:
    player = None
    cards = []

    def __init__(self, player):
        self.player = player

def print_json (self, state):
    return {
        'player': state.player.serialise(),
        'cards': [card.serialise() for card in state.cards]
    }
