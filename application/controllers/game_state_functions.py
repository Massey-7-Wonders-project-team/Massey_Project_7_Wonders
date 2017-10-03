from .database_functions import *
import random
import copy


def deal_wonders(players):
    wonders = Wonder.query.all()
    cardhists = []

    for player in players:
        wonder = wonders.pop(random.randint(0, len(wonders)-1))
        player.wonder = wonder.name
        player.max_wonder = wonder.slots

        card = Card.query.filter_by(name=wonder.card_0).first()
        update_player_object(card, player)
        cardhists.append(Cardhist(playerId=player.id, cardId=card.id, discarded=False, for_wonder=True, card_name=card.name))

    db_committing_function(p=players, c=cardhists)


def age_calcs_and_dealing(players, game):
    """Call to calculate end of age calculations
    and/or the next age's hands dealt"""
    print(game.age, " Game Age - Will Now Be Processed And Incremented")

    if game.age > 0:
        military_calcs(players, game.age)

        # Implements the babylon_2 play both cards logic
        for p in players:
            if p.play_twice:
                # Gets the final card in the player's hand and plays it
                card = get_cards(get_player(get_next_player_id(p, game.age)))[0]
                play_card(card, p, False, False, no_prereq=True)
                print(p.name + " played both cards")
                p.play_twice = False

    # End of age 3 - wrap up game
    if game.age > 2:
        game.complete = True

        for p in players:
            end_game_cards(p, get_cards(player=p, history=True))
            p.points += p.money // 3

            # Implement borrow purple card, Zeus_3 wonder card, and use the highest scoring one
            if [x for x in get_cards(player=p, history=True) if x.name == 'zeus_3']:
                purples = [x for x in get_cards(player=get_player(p.left_id), history=True) +
                           get_cards(player=get_player(p.right_id), history=True) if x.colour == 'purple']
                scores = []
                for card in purples:
                    temp = p.points
                    end_game_cards(p, card)
                    scores.append(p.points - temp)
                p.points += max(scores) - sum(scores)

        db_committing_function(p=players, g=game)
        [print(p.name, p.points) for p in players]
        print("Game Over")

    # Move onto next age
    else:
        game.round = 1
        game.age += 1
        cards = Card.query.filter(Card.noPlayers <= len(players)).filter_by(age=game.age).all()

        # Only deal enough guilds for noPlayers+2
        if game.age == 3:
            guilds = [card for card in cards if card.colour == 'purple']
            random.shuffle(guilds)
            guilds = guilds[:len(players)+2]
            cards = [card for card in cards if not card.colour == 'purple' or card in guilds]

        # Randomly assign cards to players
        dealt_cards = []
        for player in players:
            for j in range(7):
                param = random.randint(0, len(cards)-1)
                card = cards.pop(param)
                dealt_cards.append(Round(age=game.age, round=1, playerId=player.id, cardId=card.id))
        db_committing_function(d=dealt_cards, p=players, g=game)


def get_next_player_id(player, age):
    if age == 2:
        return player.right_id
    else:
        return player.left_id


def set_player_neighbours(players):
    """Called at the beginning of the game to set player's left_id and right_id"""
    num_players = len(players)
    i = num_players

    for player in players:
        player.left_id = players[(i-1) % num_players].id
        player.right_id = players[(i+1) % num_players].id
        i += 1

    db_committing_function(p=players)


def how_much_deficit(card, player):
    """
    Replaces the main logic section of check_valid_move and its helper with a bit cleaner code.
    Only used by trade functions awaiting refactor. Only considers resources (not money or other concerns)
    :param card: Card object to be played
    :param player: Player object playing the card
    :return: Tuple of boolean (whether the card is playable using the player's resources)
                and a None type if true, or a list of lists specifying what resources the player is short on
    """
    # Account for normal player resources
    balance = [card.costStone - player.stone, card.costBrick - player.brick, card.costOre - player.ore,
               card.costWood - player.wood, card.costGlass - player.glass, card.costPaper - player.paper,
               card.costCloth - player.cloth]

    if not any([x for x in balance if x > 0]):  # All resources are available with normal cards
        return True, None

    # Consider resource alternating cards
    RA_cards = [[x.giveStone, x.giveBrick, x.giveOre, x.giveWood, x.giveGlass, x.givePaper, x.giveCloth]
                for x in get_cards(player=player, history=True) if x.resourceAlternating is True]
    if RA_cards:
        combinations = []
        for RA_card in RA_cards:
            group = []
            for i in range(len(RA_card)):
                if RA_card[i] != 0:
                    temp = [0] * 7
                    temp[i] = RA_card[i]
                    group.append(temp)
            if combinations:
                combinations = [[a + b for (a, b) in zip(x, y)] for x in combinations for y in group]
            else:
                combinations = group

        # Compare RA combinations with what's needed and return results
        final_balances = [[a-b for (a,b) in zip(balance, permutation)] for permutation in combinations]
        no_deficit = any([all([False if resource > 0 else True for resource in resources]) for resources in final_balances])
        return no_deficit, final_balances
    else:
        return False, [balance]


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


def play_card(card, player, is_discarded, for_wonder, no_prereq=False):

    wondercard = None

    if is_discarded:
        player.money += 3

    elif for_wonder:
        wondercard = get_wonder_card(player)
        if no_prereq:
            print("Playing: ", wondercard.name)
            update_player_object(wondercard, player, for_wonder=True)
        elif check_valid_move(wondercard, player):
            print("Playing: ", wondercard.name)
            update_player_object(wondercard, player, for_wonder=True)
        else:
            print(wondercard.name + " is an invalid move")
            return False

        card = wondercard
        if player.wonder == "The Mausoleum of Halicarnassus":
            game = get_game(player=player)
            game.waiting_for_discard = True
            db_committing_function(game)

    elif not is_discarded and not for_wonder:
        if no_prereq: # Branch used for certain wonder bonuses
            update_player_object(card, player)
        elif check_valid_move(card, player):
            update_player_object(card, player)
        else:
            print(card.name + " is an invalid move")
            return False

    history = Cardhist(playerId=player.id, cardId=card.id, discarded=is_discarded, for_wonder=for_wonder,
                       card_name=card.name)
    db_committing_function(player, history)

    return True


def swap_hands(card, player, game):
    # UPDATE DB
    old_round_cardId = [c.id for c in get_cards(player)]
    print("Cards in hand", old_round_cardId, "    Card trying to remove:", card.id, card.name)
    old_round_cardId.remove(card.id)

    rounds = []
    for unplayed_card in old_round_cardId:
        rounds.append(
            Round(playerId=get_next_player_id(player, game.age), age=game.age, round=game.round + 1,
                  cardId=unplayed_card))

    db_committing_function(r=rounds)


def update_player_object(card, player, for_wonder=False):
    """Helper function for process_card"""
    if card.resourceAlternating:
        player.extra_brick += card.giveBrick
        player.extra_ore += card.giveOre
        player.extra_wood += card.giveWood
        player.extra_stone += card.giveStone
        player.extra_paper += card.givePaper
        player.extra_cloth += card.giveCloth
        player.extra_glass += card.giveGlass
    else:
        player.brick += card.giveBrick
        player.ore += card.giveOre
        player.wood += card.giveWood
        player.stone += card.giveStone
        player.paper += card.givePaper
        player.cloth += card.giveCloth
        player.glass += card.giveGlass

    player.military += card.giveMilitary
    player.points += card.givePoints
    player.money += card.giveMoney - card.costMoney

    if for_wonder:
        player.wonder_level += 1

    if card.giveResearch:
        research_calcs(card, player)

    if card.colour == 'wonder':
        if card.name == 'zeus_1':
            player.left_cheap_trade = True
            player.right_cheap_trade = True

        elif card.name == 'babylon_2':
            player.play_twice = True
    elif card.colour == 'grey':
        player.grey += 1
    elif card.colour == 'red':
        player.red += 1
    elif card.colour == 'green':
        player.green += 1
    elif card.colour == 'purple':
        player.purple += 1
    elif card.colour == 'blue':
        player.blue += 1
    elif card.colour == 'brown':
        player.brown += 1
    elif card.colour == 'yellow':
        player.yellow += 1
        left_player = get_player(player.left_id)
        left_player_cards = get_cards(player=left_player, history=True)
        cards = get_cards(player=player, history=True)
        right_player = get_player(player.right_id)
        right_player_cards = get_cards(player=right_player, history=True)

        if card.name == 'East Trading Post':
            player.right_cheap_trade = True

        elif card.name == 'West Trading Post':
            player.left_cheap_trade = True

        elif card.name == 'Marketplace':
            player.advanced_cheap_trade = True

        elif card.name == 'Vineyard':
            player.money += len([x for x in left_player_cards if x.colour == 'brown'])
            player.money += len([x for x in cards if x.colour == 'brown'])
            player.money += len([x for x in right_player_cards if x.colour == 'brown'])

        elif card.name == 'Bazaar':
            player.money += len([x for x in left_player_cards if x.colour == 'grey']) * 2
            player.money += len([x for x in cards if x.colour == 'grey']) * 2
            player.money += len([x for x in right_player_cards if x.colour == 'grey']) * 2

        elif card.name == 'Arena':
            player.money += 3 * player.wonder_level

        elif card.name == 'Lighthouse':
            player.money += len([x for x in cards if x.colour == 'yellow']) + 1

        elif card.name == 'Haven':
            player.money += len([x for x in cards if x.colour == 'brown'])

        elif card.name == 'Chamber of Commerce':
            player.money += len([x for x in cards if x.colour == 'grey']) * 2


def end_game_cards(player, cards):
    left_player = get_player(player.left_id)
    left_player_cards = get_cards(player=left_player, history=True)
    right_player = get_player(player.right_id)
    right_player_cards = get_cards(player=right_player, history=True)

    for card in cards:

        if card.colour == 'yellow':
            if card.name == 'Arena':
                player.points += player.wonder_level

            elif card.name == 'Lighthouse':
                player.points += len([x for x in cards if x.colour == 'yellow'])

            elif card.name == 'Haven':
                player.points += len([x for x in cards if x.colour == 'brown'])

            elif card.name == 'Chamber of Commerce':
                player.points += len([x for x in cards if x.colour == 'grey']) * 2

        elif card.colour == 'purple':
            if card.name == 'Workers Guild':
                player.points += len([x for x in left_player_cards if x.colour == 'brown'])
                player.points += len([x for x in right_player_cards if x.colour == 'brown'])

            elif card.name == 'Craftsmens Guild':
                player.points += len([x for x in left_player_cards if x.colour == 'grey']) * 2
                player.points += len([x for x in right_player_cards if x.colour == 'grey']) * 2

            elif card.name == 'Traders Guild':
                player.points += len([x for x in left_player_cards if x.colour == 'yellow'])
                player.points += len([x for x in right_player_cards if x.colour == 'yellow'])

            elif card.name == 'Magistrates Guild':
                player.points += len([x for x in left_player_cards if x.colour == 'blue'])
                player.points += len([x for x in right_player_cards if x.colour == 'blue'])

            elif card.name == 'Philosophers Guild':
                player.points += len([x for x in left_player_cards if x.colour == 'green'])
                player.points += len([x for x in right_player_cards if x.colour == 'green'])

            elif card.name == 'Spies Guild':
                player.points += len([x for x in left_player_cards if x.colour == 'red'])
                player.points += len([x for x in right_player_cards if x.colour == 'red'])

            elif card.name == 'Shipowners Guild':
                player.points += len([x for x in cards if x.colour == 'brown'])
                player.points += len([x for x in cards if x.colour == 'grey'])
                player.points += len([x for x in cards if x.colour == 'purple'])

            elif card.name == 'Builders Guild':
                player.points += left_player.wonder_level + player.wonder_level + right_player.wonder_level

            elif card.name == 'Strategists Guild':
                player.points += left_player.military_loss + right_player.military_loss


def increment_game_round(game_info, players):
    """Helper function to process_card, changes round"""
    if game_info.waiting_for_discard:
        print("Waiting for Halicarnassus to play discard")
        return

    game_info.round += 1
    db_committing_function(game=game_info)

    if game_info.round == 7:
        age_calcs_and_dealing(players, game_info)


def military_calcs(players, age):
    if age is 1:
        win = 1
    elif age is 2:
        win = 3
    elif age is 3:
        win = 5

    for player in players:
        left_player = list(filter(lambda p: p.id == player.left_id, players))[0]
        right_player = list(filter(lambda p: p.id == player.right_id, players))[0]
        if player.military > left_player.military:
            player.points += win
        elif player.military < left_player.military:
            player.points -= 1
            player.military_loss += 1

        if player.military > right_player.military:
            player.points += win
        elif player.military < right_player.military:
            player.points -= 1
            player.military_loss += 1


def research_calcs(card, player):
    """Updates points given by research - computes difference between old and new points"""
    old_points = research_helper(player)

    if card.giveResearch == 'cog':
        player.cog += 1
    elif card.giveResearch == 'tablet':
        player.tablet += 1
    elif card.giveResearch == 'compass':
        player.compass += 1
    elif card.giveResearch == 'wildcard':
        player.wildcard += 1

    new_points = research_helper(player)
    player.points += new_points - old_points


def research_helper(player):
    """Called by research_calcs
    Returns an int representing points attributed to research cards"""
    research = [player.cog, player.tablet, player.compass]

    if player.wildcard > 0:
        # Searches for optimal use of wildcard
        points = []
        research_helpers_rec_search(points, player.wildcard, research)
        return max(points, default=0)
    else:
        return min(research) * 7 + sum([r * r for r in research])


def research_helpers_rec_search(points, wildcards, research):
    """Searches optimal combination of wildcards with existing research cards
    Populates points list with results which research_helper uses"""
    if wildcards is 0:
        points.add(min(research) * 7 + sum([r * r for r in research]))
        return

    new_research = copy.deepcopy(research)

    for j in range(wildcards):
        for i in range(len(research)):
            new_research[i] += 1
            wildcards -= 1
            research_helpers_rec_search(points, wildcards, new_research)

            # Roll back changes
            wildcards += 1
            new_research[i] -= 1
