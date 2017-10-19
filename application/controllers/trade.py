from .database_functions import *
import copy


def check_move_and_trade(card, player):
    # Get cards (yellow and non-base resource wonder cards are not used for trade)
    cards = [c for c in get_cards(player=player, history=True)]
    default_false = {'left': {'cost': 0}, 'right': {'cost': 0}, 'possible': False, 'message': ''}
    default_true = {'left': {'cost': 0}, 'right': {'cost': 0}, 'possible': True, 'message': ''}

    # Checks there is not already one of this card played yet
    if [x for x in cards if x.name == card.name]:
        default_false['message'] = 'You already have a {} card. Only one of each type may be played'.format(card.name)
        return default_false

    # Checks if card can be played using prerequisites
    prereq = [x.name for x in cards if card.prerequisite1 == x.name or card.prerequisite2 == x.name]
    if prereq:
        default_true['message'] = 'You use the {} prereq card to buy this card for free'.format(prereq[0])
        return default_true

    # Check money
    if card.costMoney > player.money:
        default_false['message'] = 'You only have {} money of the {} required'.format(player.money, card.costMoney)
        return default_false

    # Process cards into queue
    needed = get_card_requirements(card)
    card_options = []
    create_list(cards, card_options, [0, 0], 'player')
    left_cards = [c for c in get_cards(player=get_player(player.left_id), history=True) if not c.colour == 'yellow'
                  and not c.colour == 'wonder' or c.colour == 'wonder' and c.name.endswith('_0')]
    right_cards = [c for c in get_cards(player=get_player(player.right_id), history=True) if not c.colour == 'yellow'
                   and not c.colour == 'wonder' or c.colour == 'wonder' and c.name.endswith('_0')]
    create_list(left_cards, card_options,
                [1 if player.left_cheap_trade else 2, 1 if player.advanced_cheap_trade else 2], 'left')
    create_list(right_cards, card_options,
                [1 if player.right_cheap_trade else 2, 1 if player.advanced_cheap_trade else 2], 'right')
    card_options = sorted(card_options, key=lambda k: k[list(k.keys())[0]][1]
                            if k[list(k.keys())[0]] != 'Alternating' else k[list(k.keys())[1]][1])

    # Discard cards not needed
    prune_cards(needed, card_options)

    # Allocate resources
    stats = []
    assign_cards(card_options, needed, 0, stats, default_false)

    # Returns best option if successful or default if check fails
    price = stats[0]['left']['cost'] + stats[0]['right']['cost']
    if stats and price <= player.money:
        return stats[0]
    elif stats:
        info = stats[0]
        info['possible'] = False
        info['message'] = 'You do not have enough money for this trade. {} gold is required'.format(price)
        return info
    else:
        default_false['message'] = "The necessary resources are not available in your or your neighbours' civilisations"
        return default_false


def assign_cards(card_options, needed, current_price, stats, tempstats):
    while card_options and any(needed):
        # If this branch has reached the price of the best option, prune
        if stats and tempstats['left']['cost'] + tempstats['right']['cost'] >= stats[0]['left']['cost'] + stats[0]['right']['cost']:
            return
        print("Needed:", needed)

        # Choose next card to play. Favour non RA cards where price is equal
        c = None
        index = 0
        while not c:
            if len(card_options) > index:
                temp = card_options[index]
                for i in temp.keys():
                    if i != 'Alternating' and temp[i][1] > current_price:
                        c = card_options.pop(0)
                        current_price = c[i][1]
                        break
                    elif i != 'Alternating' and temp[i][1] == current_price:
                        c = card_options.pop(index)
                        break
                    else:
                        break
            else:
                print("else branch of choosing card")
                c = card_options.pop(0)
                for i in temp.keys():
                    if i != 'Alternating':
                        current_price = c[i][1]
                        break
            index += 1

        # Process card
        if c['Alternating']:
            for key in temp.keys():
                if key != 'Alternating':
                    stripped = {key: temp[key]}
                    new_needed = copy.deepcopy(needed)
                    new_card_options = copy.deepcopy(card_options)
                    new_tempstats = copy.deepcopy(tempstats)
                    use_card(stripped, new_needed, new_card_options, new_tempstats)
                    assign_cards(new_card_options, new_needed, current_price, stats, new_tempstats)
        else:
            use_card(c, needed, card_options, tempstats)

    # Checks if this combination solves problem. If it does, it places on priority queue
    if not any(needed):
        tempstats['possible'] = True
        if stats and tempstats['left']['cost'] + tempstats['right']['cost'] < stats[0]['left']['cost'] + stats[0]['right']['cost']:
            stats.insert(0, tempstats)
        else:
            stats.append(tempstats)


def use_card(card, needed, card_options, stats):
    for t in card.keys():
        if t in needed.keys():
            needed[t] -= card[t][0]

            # Update stats with other player's resources if used
            if card[t][2] != 'player':
                used = card[t][0] + needed[t] if needed[t] < 0 else card[t][0]
                try:
                    stats[card[t][2]][t] += used
                except Exception as e:
                    stats[card[t][2]][t] = used
                try:
                    stats[card[t][2]]['cost'] += used * card[t][1]
                except Exception as e:
                    stats[card[t][2]]['cost'] = used * card[t][1]

            # If resource requirement is satisfied, prune unneeded cards
            if not needed[t] > 0:
                needed.pop(t)
                prune_cards(needed, card_options)


def prune_cards(needed, card_options):
    needed_types = needed.keys()

    for card in card_options:
        temp = []
        for key in card.keys():
            if key not in needed_types and not key == 'Alternating':
                temp.append(key)
        [card.pop(key) for key in temp]
        temp = card.keys()
        if len(temp) == 1:
            card_options.remove(card)
        elif len(temp) == 2 and card['Alternating'] is True:
            card['Alternating'] = False


def create_list(cards, array, cost, player):
    for c in cards:
        temp = get_card_benefits(c, cost, player)
        if len(temp) > 1:
            array.append(temp)


def get_card_requirements(card):
    temp = {}
    if card.costStone:
        temp['Stone'] = card.costStone
    if card.costBrick:
        temp['Brick'] = card.costBrick
    if card.costOre:
        temp['Ore'] = card.costOre
    if card.costWood:
        temp['Wood'] = card.costWood
    if card.costGlass:
        temp['Glass'] = card.costGlass
    if card.costPaper:
        temp['Paper'] = card.costPaper
    if card.costCloth:
        temp['Cloth'] = card.costCloth
    return temp


def get_card_benefits(card, prices, player):
    temp = {}
    if card.giveStone:
        temp['Stone'] = [card.giveStone, prices[0], player]
    if card.giveBrick:
        temp['Brick'] = [card.giveBrick, prices[0], player]
    if card.giveOre:
        temp['Ore'] = [card.giveOre, prices[0], player]
    if card.giveWood:
        temp['Wood'] = [card.giveWood, prices[0], player]
    if card.giveGlass:
        temp['Glass'] = [card.giveGlass, prices[1], player]
    if card.givePaper:
        temp['Paper'] = [card.givePaper, prices[1], player]
    if card.giveCloth:
        temp['Cloth'] = [card.giveCloth, prices[1], player]
    if card.resourceAlternating:
        temp['Alternating'] = True
    else:
        temp['Alternating'] = False
    return temp
