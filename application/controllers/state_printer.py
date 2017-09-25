from .database_functions import *


def print_json(player, players=None, cards=None, history=None, game=None):

    if not players:
        players = get_players(player.gameId)
    if not cards:
        cards = get_cards(player=player)
    if not history:
        history = get_card_history(player)
    if not game:
        game = get_game(player=player)

    return {
        'game': game.serialise(),
        'player': player.serialise(),
        'allPlayers': [p.serialise() for p in players if p != player],
        'history': [h.serialise() for h in history],
        'cards': [card.serialise() for card in cards],
    }


def false_true (string):
    if string == 'false':
        return False
    elif string == 'true':
        return True
    elif string is True or string is False:
        return string

    if not string:
        print(string + " given into false_true function")
    else:
        print(string)

