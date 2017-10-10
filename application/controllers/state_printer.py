from .database_functions import *


def print_json(player, players=None, cards=None, game=None):

    if not players:
        players = get_players(player.gameId)
    if not cards:
        cards = get_cards(player=player)
    if not game:
        game = get_game(player=player)

    if game.waiting_for_discard and player.wonder == "The Mausoleum of Halicarnassus":
        discarded_cards = get_all_discarded_cards(player)
        return {
            'game': game.serialise(),
            'player': player.serialise(),
            'allPlayers': [p.serialise() for p in players if p != player],
            'history': [[h.serialise() for h in get_cards(player=p, history=True)] for p in players],
            'cards': [card.serialise() for card in cards],
            'discarded': [discarded.serialise() for discarded in discarded_cards]
        }
    else:
        return {
            'game': game.serialise(),
            'player': player.serialise(),
            'allPlayers': [p.serialise() for p in players if p != player],
            'history': [[h.serialise() for h in get_cards(player=p, history=True)] for p in players],
            'cards': [card.serialise() for card in cards],
        }


def false_true (string):
    if not string:
        return None
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
