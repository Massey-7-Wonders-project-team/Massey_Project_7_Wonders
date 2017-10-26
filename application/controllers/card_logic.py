# Card_helpers and Setup_game use some of these import statements
# Card_logic is considered the main controller class

from .game_state_functions import *
from .ai import *


def process_card(card, player, is_discarded, for_wonder, from_discard_pile=None, process_with_trade=True):
    """Called from play_card API endpoint, plays card, updates DB, and checks if able to go to next turn
    Returns false if card unable to be played, otherwise true"""
    game_info = get_game(player=player)
    players = (Player.query.filter_by(gameId=player.gameId)).all()

    if from_discard_pile:
        stats = play_card_with_trade(card, player, False, False, no_prereq=True)
        game_info.waiting_for_discard = False
        db_committing_function(game_info)

    else:
        # Guards against more than one card being played in a round
        if Round.query.filter_by(age=game_info.age, round=game_info.round+1, playerId=get_next_player_id(player, game_info.age)).all():
            print("Card already played this round")
            return {'left': {'cost': 0}, 'right': {'cost': 0}, 'possible': False, 'message': 'Card already played this round'}

        # Guards against playing cards that are not in the current hand
        if not [c for c in get_cards(player=player) if c == card]:
            print(str(card.name) + " is not part of this hand")
            return {'left': {'cost': 0}, 'right': {'cost': 0}, 'possible': False, 'message': '{} is not part of this hand'.format(card.name)}

        # Attempts to play the card. Returns info to player if trade is needed (and not confirmed) or move is invalid
        stats = play_card_with_trade(card, player, is_discarded, for_wonder, process_with_trade)
        if not stats['possible'] or stats['left']['cost'] + stats['right']['cost'] > 0 and not process_with_trade:
            return stats

        # Gives hand to next player
        swap_hands(card, player, game_info)

        # TURN COMPLETION LOGIC
        # AI players play if single player
        if game_info.single_player and not player.ai:
            for p in [p for p in players if p != player]:
                ai_move(p, game_info)

    for p in players:
        query = Round.query.filter_by(age=game_info.age, round=game_info.round+1, playerId=p.id).all()
        if not query:
            print("Does not increment round - Player", str(p.id), "still needs to play")
            return stats

    # Only triggers if all players have finished their turn
    print("Increments round")
    increment_game_round(game_info, players)
    return stats


def ai_move(player, game):
    """
    All AI play round. Currently they just play the first card they can. Difficulty -100 ;)
    :param player: Non-human player
    :param game: Game object
    :return: No return
    """
    cards = get_cards(player=player, game=game)

    # Tries to play the first available card
    for card in cards:
        if play_card(card, player, False, False):
            swap_hands(card, player, game)
            return

    # No cards can be played, so discards one
    play_card(cards[0], player, True, False)
    swap_hands(card, player, game)
