# Card_helpers and Setup_game use some of these import statements
# Card_logic is considered the main controller class

from .game_state_functions import *
from .ai import *


def process_card(card, player, is_discarded, for_wonder, play_discard=None, trade=True):
    """Called from play_card API endpoint, plays card, updates DB, and checks if able to go to next turn
    Returns false if card unable to be played, otherwise true"""
    game_info = get_game(player=player)
    players = (Player.query.filter_by(gameId=player.gameId)).all()

    if play_discard:
        play_card(card, player, False, False, no_prereq=True)
        game_info.waiting_for_discard = False
        db_committing_function(game_info)

    else:
        # Guards against more than one card being played in a round
        if Round.query.filter_by(age=game_info.age, round=game_info.round+1, playerId=get_next_player_id(player, game_info.age)).all():
            print("Card already played this round")
            return False

        # Guards against playing cards that are not in the current hand
        if not [c for c in get_cards(player=player) if c == card]:
            print(str(card.name) + " is not part of this hand")
            return False

        # Attempts to play the card
        if not play_card(card, player, is_discarded, for_wonder):
            if trade:
                success, info = calculate_trades(card, player)
                if not success or info['total_cost'] > player.money:
                    return False

                play_card(card, player, False, for_wonder, no_prereq=True)
                player.money -= info['total_cost']
                player_left = get_player(player.left_id).money
                player_left += info['left_cost']
                player_right = get_player(player.right_id).money
                player_right += info['right_cost']
                db_committing_function(player, player_left, player_right)

                print("Trade used for card: ", card.name)
                print("Costs", info)

            else:
                return False

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
            return True

    # Only triggers if all players have finished their turn
    print("Increments round")
    increment_game_round(game_info, players)
    return True


def calculate_trades(card, player):
    """
    :param card: Card to be played
    :param player: Player playing the card
    :return: None if no trade needed, else a dict itemising the optimal trade
    """
    # Figure out if trade is required.
    # Resources_needed is a list of lists of what was missing during that branch of recursion
    no_trade_needed, resources_needed = how_much_deficit(card, player)

    if no_trade_needed:
        print("No trade needed")
        return True, None

    # Get neighbouring resources
    left_player = get_player(player.left_id)
    right_player = get_player(player.right_id)
    left_balance = [left_player.stone, left_player.brick, left_player.ore, left_player.wood, left_player.glass,
                    left_player.paper, left_player.cloth]
    right_balance = [right_player.stone, right_player.brick, right_player.ore, right_player.wood,
                     right_player.glass, right_player.paper, right_player.cloth]
    left_ra_cards = [[x.giveStone, x.giveBrick, x.giveOre, x.giveWood, x.giveGlass, x.givePaper, x.giveCloth]
                     for x in get_cards(left_player, history=True) if x.resourceAlternating]
    right_ra_cards = [[x.giveStone, x.giveBrick, x.giveOre, x.giveWood, x.giveGlass, x.givePaper, x.giveCloth]
                      for x in get_cards(right_player, history=True) if x.resourceAlternating]

    # RA card combos
    left_RA_combinations = []
    right_RA_combinations = []
    for RA_card in left_ra_cards:
        group = []
        for i in range(len(RA_card)):
            if RA_card[i] != 0:
                temp = [0] * 7
                temp[i] = RA_card[i]
                group.append(temp)
        if left_RA_combinations:
            left_RA_combinations = [[a + b for (a, b) in zip(x, y)] for x in left_RA_combinations for y in group]
        else:
            left_RA_combinations = group
    for RA_card in right_ra_cards:
        group = []
        for i in range(len(RA_card)):
            if RA_card[i] != 0:
                temp = [0] * 7
                temp[i] = RA_card[i]
                group.append(temp)
        if right_RA_combinations:
            right_RA_combinations = [[a + b for (a, b) in zip(x, y)] for x in left_RA_combinations for y in group]
        else:
            right_RA_combinations = group

    # Populate trading choices
    trade_choices = []
    for combination in resources_needed:
        combo = search_trade_options(player, combination, left_balance, right_balance,
                                     left_RA_combinations, right_RA_combinations)
        trade_choices.append(combo)

    # Evaluate best choice and return the dictionary of the best combination
    prices = [x['total_cost'] for x in trade_choices if x['possible']]
    if prices:  # Success
        min_price = min(prices)
        return True, [choice for choice in trade_choices if choice['total_cost'] == min_price][0]
    else:  # Failure - no trade options
        return False, None


def search_trade_options(player, c, left_balance, right_balance, left_ra_cards, right_ra_cards):
    """
    :param player: Player object who needs the trade
    :param c: 7 element list of what resources are needed for trade
    :param left_balance: Normal resources that the left player has (7 element list)
    :param right_balance: Normal resources that the right player has (7 element list)
    :param left_ra_cards: RA resources that the left player has. Each sublist is one combination of RA cards (list of 7 element lists)
    :param right_ra_cards: RA resources that the right player has. Each sublist is one combination of RA cards (list of 7 element lists)
    :return: The combo dict shown below
    """

    # Set data structure
    combo = {'left': [0, 0, 0, 0, 0, 0, 0],
             'right': [0, 0, 0, 0, 0, 0, 0],
             'left_cost': 0,
             'right_cost': 0,
             'total_cost': 0,
             'possible': False}
    c = [x if x > 0 else 0 for x in c]  # Make all elements in c non-negative

    # Run calculations
    if player.right_cheap_trade and not player.left_cheap_trade:
        # Right basic resources
        trade_updater(player, combo, c, right_balance, advanced=False, left=False)
        # Right RA basic resources
        best = get_best_RA_combo(c, right_ra_cards)
        trade_updater(player, combo, c, best, advanced=False, left=False)
        # Left all resources
        trade_updater(player, combo, c, left_balance, left=True)
        # Left RA resources
        best = get_best_RA_combo(c, left_ra_cards)
        trade_updater(player, combo, c, best, advanced=False)
        best = get_best_RA_combo(c, left_ra_cards, basic=False)
        trade_updater(player, combo, c, best, basic=False)
        # Right advanced resources
        trade_updater(player, combo, c, right_balance, basic=False, left=False)
        # Right RA advanced resources
        best = get_best_RA_combo(c, right_ra_cards, basic=False)
        trade_updater(player, combo, c, best, basic=False, left=False)

    else:
        # Left resources
        trade_updater(player, combo, c, left_balance)
        # Left RA resources
        best = get_best_RA_combo(c, left_ra_cards)
        trade_updater(player, combo, c, best, advanced=False)
        best = get_best_RA_combo(c, left_ra_cards, basic=False)
        trade_updater(player, combo, c, best, basic=False)
        # Right resources
        trade_updater(player, combo, c, right_balance, left=False)
        # Right RA resources
        best = get_best_RA_combo(c, right_ra_cards)
        trade_updater(player, combo, c, best, advanced=False)
        best = get_best_RA_combo(c, right_ra_cards, basic=False)
        trade_updater(player, combo, c, best, basic=False)

    # Return results
    if not combo['possible'] and not [x for x in c if x > 0]:
        combo['possible'] = True
    combo['total_cost'] = combo['left_cost'] + combo['right_cost']
    return combo


def get_best_RA_combo(c, list_cards, basic=True):
    """
    Assumes no RA cards have both basic and advanced resources.
    Without considering combinations of both left and right players' RA cards, it is technically possible to
    return a non-optimal solution, but should happen so infrequently as to not be worth doing. Monitor and change
    if it happens a noticeable amount of times.
    :param c: A 7 element list of what is needed
    :param list_cards: A list of 7 element lists specifying possible combinations
    :param basic: If true, returns the best combination of basic resources, otherwise of advanced resources
    :return: Returns best 7 element list
    """
    if not list_cards:
        return None
    if basic:
        usage = [sum([a if a < b else b for (a, b) in zip(x[0:4], c[0:4])]) for x in list_cards]
        best_index = usage.index(max(usage))
    else:
        usage = [sum([a if a < b else b for (a, b) in zip(x[4:], c[4:])]) for x in list_cards]
        best_index = usage.index(max(usage))

    return list_cards[best_index]


def trade_updater(player, combo, c, cards, basic=True, advanced=True, left=True):
    """
    This function updates the combo dict based on the settings provided
    :param player: Player object
    :param combo: Combo dict specified in search trade options
    :param c: 7 element list specifying what is still needed
    :param cards: 7 element list specifying what resources can be provided
    :param basic: Optional, if False, Brick, Wood, Stone and Ore are not updated
    :param advanced: Optional, if False, Glass, Paper and Cloth are not updated
    :param left: Optional, if False, the card is assumed to come from the right player (not the default left)
    :return: No return. C and combo are changed in situ
    """
    if not cards:
        return

    # Are we done yet?
    if combo['possible']:
        return
    elif not [x for x in c if x > 0]:  # Triggers if there are no outstanding resource needs in c
        combo['possible'] = True
        return

    if basic:
        used = [x if y > x else y for (x, y) in zip(c[0:4], cards[0:4])]
        c[0:4] = [y-x for (x, y) in zip(used, c)]  # Use resources
        if left:
            combo['left'][0:4] = [x+y for (x, y) in zip(used, combo['left'])]
            combo['left_cost'] += sum(used) if player.left_cheap_trade else sum(used) * 2
        else:
            combo['right'][0:4] = [x+y for (x, y) in zip(used, combo['right'])]
            combo['right_cost'] += sum(used) if player.right_cheap_trade else sum(used) * 2

    if advanced:
        used = [x if y > x else y for (x, y) in zip(c[4:], cards[4:])]
        c[4:] = [y-x for (x, y) in zip(used, c[4:])]   # Use resources
        if left:
            combo['left'][4:] = [x+y for (x, y) in zip(used, combo['left'][4:])]
            combo['left_cost'] += sum(used) if player.advanced_cheap_trade else sum(used) * 2
        else:
            combo['right'][4:] = [x+y for (x, y) in zip(used, combo['right'][4:])]
            combo['right_cost'] += sum(used) if player.advanced_cheap_trade else sum(used) * 2


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
