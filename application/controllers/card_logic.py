# Card_helpers and Setup_game use some of these import statements
# Card_logic is considered the main controller class

from .game_state_functions import *
from .ai import *


def get_next_player_id(player, age):
    if age == 2:
        return player.right_id
    else:
        return player.left_id


def resource_alternating_rec_search(balance, cards):
    """Helper function for check_move. Checks resource permutations for alternating resource cards
     Returns False if not possible, True if possible"""
    if not list(filter(lambda x: x > 0, balance)):
        return True
    if not cards:
        return False

    new_cards = copy.deepcopy(cards)
    new_bal = copy.deepcopy(balance)

    for card in new_cards:
        new_cards = new_cards[1:]

        for i in range(len(balance)):
            if balance[i] > 0 and card[i] > 0:
                new_bal[i] -= card[i]
                if resource_alternating_rec_search(new_bal, new_cards):
                    return True
                else:
                    # Roll back changes from iteration
                    new_bal[i] += card[i]

    # Search sub-space exhausted without success
    return False


def check_valid_move(card, player):
    """Call before processing card to check that it is a valid move, returns boolean"""

    history = get_cards(player=player, history=True)

    # Checks there is not already one of this card played yet
    if [x for x in history if x.name == card.name]:
        return False

    # Checks if card can be played using prerequisites
    if [x for x in history if card.prerequisite1 == x.name or card.prerequisite2 == x.name]:
        return True

    # Check money
    if card.costMoney > player.money:
        print("not enough money")
        return False

    balance = [card.costStone - player.stone, card.costBrick - player.brick, card.costOre - player.ore,
               card.costWood - player.wood, card.costGlass - player.glass, card.costPaper - player.paper,
               card.costCloth - player.cloth]

    # If true, there are materials missing, and checks for resource alternating materials ensues
    if list(filter(lambda x: x > 0, balance)):
        extra = [player.extra_stone, player.extra_brick, player.extra_ore, player.extra_wood, player.extra_glass,
                 player.extra_paper, player.extra_cloth]
        maximum = [x-y for (x,y) in zip(balance, extra)]

        # Investigates if there is a permutation that will work after checking that there could be a chance of success
        if list(filter(lambda x: x > 0, maximum)):
            return False
        else:
            ra_cards = [[x.giveStone, x.giveBrick, x.giveOre, x.giveWood, x.giveGlass, x.givePaper, x.giveCloth]
                        for x in history if x.resourceAlternating]
            return resource_alternating_rec_search(balance, ra_cards)

    # Triggers if there are enough materials without considering resource alternation
    else:
        return True


def prepare_db_changes_after_turn(card, player, is_discarded, for_wonder, game_info):

    old_round_cardId = [c.id for c in get_cards(player)]
    print("Cards in hand", old_round_cardId, "    Card trying to remove:", card.id)
    old_round_cardId.remove(card.id)

    history = Cardhist(playerId=player.id, cardId=card.id, discarded=is_discarded, for_wonder=for_wonder, card_name=card.name)

    rounds = []
    for unplayed_card in old_round_cardId:
        rounds.append(Round(playerId=get_next_player_id(player, game_info.age), age=game_info.age, round=game_info.round + 1,
                            cardId=unplayed_card))

    db_committing_function(p=player, h=history, r=rounds)


def process_card(card, player, is_discarded, for_wonder):
    """Called from play_card API endpoint, plays card, updates DB, and checks if able to go to next turn
    Returns false if card unable to be played, otherwise true"""
    game_info = get_game(player=player)

    # Guards against more than one card being played in a round
    if Round.query.filter_by(age=game_info.age, round=game_info.round+1, playerId=get_next_player_id(player, game_info.age)).all():
        print("Card already played this round")
        return False

    # Guards against playing cards that are not in the current hand
    if not [c for c in get_cards(player=player) if c == card]:
        print(str(card.name) + " is not part of this hand")
        return False

    # Play card
    if is_discarded:
        print(str(card.name) + " is discarded")
        player.money += 3
    else:
        if for_wonder:
            # use wonder card instead of played card
            print(str(card.name) + " is used for wonder")
            card = get_wonder_card(player)
        if not card or check_valid_move(card, player) is False:
            print(str(card.name) + " is not a valid move (insufficient resources/prerequisites or already played card with same name)")
            return False
        print(str(card.name) + " is used for wonder or is processed")
        update_player_object(card, player, for_wonder)

    # UPDATE DB
    prepare_db_changes_after_turn(card, player, is_discarded, for_wonder, game_info)

    # TURN COMPLETION LOGIC
    players = (Player.query.filter_by(gameId=player.gameId)).all()

    # AI players play if single player
    if game_info.single_player and not player.ai:
        ai_move([p for p in players if p != player], game_info)

    for p in players:
        query = Round.query.filter_by(age=game_info.age, round=game_info.round+1, playerId=p.id).all()
        if not query:
            print("Does not increment round - Player", str(p.id), "still needs to play")
            return True

    # Only triggers if all players have finished their turn
    print("Increments round")
    increment_game_round(game_info, players)
    return True


def ai_move(ai_players, game):
    """
    All AI play round. Currently they just play the first card they can. Difficulty -100 ;)
    :param ai_players: All non-human players in list
    :param game: Game object
    :return: No return
    """
    for player in ai_players:
        cards = get_cards(player=player, game=game)

        for card in cards:
            if process_card(card, player, False, False):
                break
        process_card(cards[0], player, True, False)
