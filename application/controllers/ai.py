from .database_functions import *
from .card_logic import *
import random

def rank_move(player, card, round, trade_dict):
    """ 
    ranks how good a certain card is to play
    used by the ai to choose next move
    higher score corresponds to a better move
    3 points roughly corresponds to 1 point
    """
    
    score = 0
    neighbours = [get_player(player.left_id), get_player(player.right_id)]
    
    #costs
    score -= card.costMoney
    
    #penalty for losing money to trade
    score -= trade_dict['left']['cost'] + trade_dict['right']['cost']

    # Gather resources
    
    '''WEIGHTS'''
        #resource weights
    grey_resources = 10
    brown_resources = 5
    extra_resources = 0.8
    resourceAlternating = 0.7
        #other weights
    points_weight = 3
    military_weight = 1.5*round #gets more important near end of round
    research_weight = 3
    if card.age == 1:
        research_weight += (12-round)/2 #bonus for getting into it early
    set_weight = 0.1
    normal_trade_weight = 1.5
    advanced_trade_weight = 2
    potential_weight = 0.2
    
    #resource cards aren't as good if you have cheap trade
    if player.left_cheap_trade:
        brown_resources /= 2
    if player.right_cheap_trade:
        brown_resources /= 2
    if player.advanced_cheap_trade:
        grey_resources /= 4
    if (player.cog + player.tablet + player.compass + player.wildcard) >= 1 and card.age == 1:
        grey_resources *= 1.5 #need more if going science
    
    if not card.resourceAlternating:
        #only need 1 of each grey
        score += max([card.giveGlass - (player.glass + player.extra_glass*extra_resources), 0])*grey_resources
        score += max([card.givePaper - (player.paper + player.extra_paper*extra_resources), 0])*grey_resources
        score += max([card.giveCloth - (player.cloth + player.extra_cloth*extra_resources), 0])*grey_resources
        
        #need 3 of these
        score += max([3*card.giveStone - (player.stone + player.extra_stone*extra_resources), 0])*brown_resources
        score += max([3*card.giveOre - (player.ore + player.extra_ore*extra_resources), 0])*brown_resources
        score += max([3*card.giveBrick - (player.brick + player.extra_brick*extra_resources), 0])*brown_resources
        score += max([3*card.giveWood - (player.wood + player.extra_wood*extra_resources), 0])*brown_resources
    else:
        #slightly less valuable, but counted twice
        #only need 1 of each grey
        score += max([card.giveGlass - (player.glass + player.extra_glass*extra_resources), 0])*grey_resources*resourceAlternating
        score += max([card.givePaper - (player.paper + player.extra_paper*extra_resources), 0])*grey_resources*resourceAlternating
        score += max([card.giveCloth - (player.cloth + player.extra_cloth*extra_resources), 0])*grey_resources*resourceAlternating
        
        #need 3 of these
        score += max([3*card.giveStone - (player.stone + player.extra_stone*extra_resources), 0])*brown_resources*resourceAlternating
        score += max([3*card.giveOre - (player.ore + player.extra_ore*extra_resources), 0])*brown_resources*resourceAlternating
        score += max([3*card.giveBrick - (player.brick + player.extra_brick*extra_resources), 0])*brown_resources*resourceAlternating
        score += max([3*card.giveWood - (player.wood + player.extra_wood*extra_resources), 0])*brown_resources*resourceAlternating

    # Score
    score += card.givePoints * points_weight

    # Military - extra points if military is close between neighbours
    if card.giveMilitary > 0:
        for n in neighbours:
            if player.military - n.military > card.giveMilitary:
                #your military is too high to be worth adding more
                score += 0
            elif player.military - n.military > 0:
                #your military is high, but still worth reinforcing
                score += card.giveMilitary*military_weight
            elif player.military - n.military > -card.giveMilitary:
                #getting this card will win you the battle!
                score += 2*card.giveMilitary*military_weight
            elif player.military - n.military > -2*card.giveMilitary:
                #this card won't be enough, but might be worth trying to get there?
                score += card.giveMilitary*military_weight
            else:
                #opponent too far ahead, don't bother trying
                score += 0

    # wonder_cards = get_all_wonder_cards(player)

    # Add bonus for lots of research cards
    if card.colour == 'green':
        #bonus to get ai to build sicence at all
        if (player.glass + player.paper + player.cloth >= 2 or player.advanced_cheap_trade) and card.age == 1:
            score += 4*research_weight
        #number of research cards increases viability for more
        score += (player.cog + player.tablet + player.compass + player.wildcard)*research_weight
        #preference for complete set > biggest symbol > other
        if card.giveResearch == 'cog':
            if player.cog < player.tablet and player.cog < player.compass:
                score *= 1 + 2*set_weight
            elif player.cog > player.tablet and player.cog > player.compass:
                score *= 1 + set_weight
        if card.giveResearch == 'tablet':
            if player.tablet < player.cog and player.tablet < player.compass:
                score *= 1 + 2*set_weight
            elif player.tablet > player.cog and player.tablet > player.compass:
                score *= 1 + set_weight
        if card.giveResearch == 'compass':
            if player.compass < player.tablet and player.compass < player.cog:
                score *= 1 + 2*set_weight
            elif player.compass > player.tablet and player.compass > player.cog:
                score *= 1 + set_weight
    elif card.name == 'Scientists Guild':
        #more appropriate here than in guild section
        if player.glass + player.paper + player.cloth + int(player.advanced_cheap_trade) >= 2:
            score += 3*research_weight
        score += (player.cog + player.tablet + player.compass + player.wildcard)*research_weight
        score += 1 + 2*set_weight #always fits in best spot

    # Yellow/purple card treatment
    
    score += card.giveMoney
    if card.giveMoney and player.money < 2*card.age:
        #bonus when low on money
        score += 2*card.age - player.money
    
    if card.colour == 'yellow':
        if card.name == 'Marketplace':
            if player.glass == 0 and (neighbours[0].glass > 0 or neighbours[1].glass > 0):
                score += advanced_trade_weight
            if player.paper == 0 and (neighbours[0].paper > 0 or neighbours[1].paper > 0):
                score += advanced_trade_weight
            if player.cloth == 0 and (neighbours[0].cloth > 0 or neighbours[1].cloth > 0):
                score += advanced_trade_weight
                
        elif card.name == 'West Trading Post':
            score += max([3*neighbours[0].stone - (player.stone + player.extra_stone*extra_resources), 0])*normal_trade_weight
            score += max([3*neighbours[0].ore - (player.ore + player.extra_ore*extra_resources), 0])*normal_trade_weight
            score += max([3*neighbours[0].brick - (player.brick + player.extra_brick*extra_resources), 0])*normal_trade_weight
            score += max([3*neighbours[0].wood - (player.wood + player.extra_wood*extra_resources), 0])*normal_trade_weight
        elif card.name == 'East Trading Post':
            score += max([3*neighbours[1].stone - (player.stone + player.extra_stone*extra_resources), 0])*normal_trade_weight
            score += max([3*neighbours[1].ore - (player.ore + player.extra_ore*extra_resources), 0])*normal_trade_weight
            score += max([3*neighbours[1].brick - (player.brick + player.extra_brick*extra_resources), 0])*normal_trade_weight
            score += max([3*neighbours[1].wood - (player.wood + player.extra_wood*extra_resources), 0])*normal_trade_weight
            
        elif card.name == 'Vineyard':
            if card.giveMoney and player.money < 2*card.age:
                #bonus when low on money
                score += 2*card.age - player.money
            score += player.brown + neighbours[0].brown + neighbours[1].brown
        elif card.name == 'Bazaar':
            if card.giveMoney and player.money < 2*card.age:
                #bonus when low on money
                score += 2*card.age - player.money
            score += 2*(player.grey + neighbours[0].grey + neighbours[1].grey)
            
        elif card.name == 'Haven':
            if card.giveMoney and player.money < 2*card.age:
                #bonus when low on money
                score += 2*card.age - player.money
            score += 4*player.brown
        elif card.name == 'Chamber Of Commerce':
            if card.giveMoney and player.money < 2*card.age:
                #bonus when low on money
                score += 2*card.age - player.money
            score += 8*player.grey
        elif card.name == 'Lighthouse':
            if card.giveMoney and player.money < 2*card.age:
                #bonus when low on money
                score += 2*card.age - player.money
            score += 4*player.yellow
            #potential for more
            score += potential_weight*(6-round)
        elif card.name == 'Arena':
            if card.giveMoney and player.money < 2*card.age:
                #bonus when low on money
                score += 2*card.age - player.money
            score += 6*player.wonder_level
            #potential for more
            score += potential_weight*(6-round)
    
    if card.colour == 'purple': 
        if card.name == 'Workers Guild':
            score += 3*(neighbours[0].brown + neighbours[1].brown)
        elif card.name == 'Craftmens Guild':
            score += 6*(neighbours[0].grey + neighbours[1].grey)
        elif card.name == 'Traders Guild':
            score += 3*(neighbours[0].yellow + neighbours[1].yellow)
            #potential for more
            score += potential_weight*(6-round)
        elif card.name == 'Philosophers Guild':
            score += 3*(neighbours[0].green + neighbours[1].green)
            #potential for more
            score += potential_weight*(6-round)
        elif card.name == 'Spies Guild':
            score += 3*(neighbours[0].red + neighbours[1].red)
            #potential for more
            score += potential_weight*(6-round)
        elif card.name == 'Magistrates Guild':
            score += 3*(neighbours[0].blue + neighbours[1].blue)
            #potential for more
            score += potential_weight*(6-round)
            
        elif card.name == 'Builders Guild':
            score += 3*(player.wonder_level + neighbours[0].wonder_level + neighbours[1].wonder_level)
            #potential for more
            score += potential_weight*(6-round)
        
        elif card.name == 'Strategists Guild':
            score += 3*(neighbours[0].military_loss + neighbours[1].military_loss)
            #potential for more
            score += potential_weight*(6-round)
        
        elif card.name == 'Shipowners Guild':
            score += 3*(player.brown + player.grey + player.purple)
            #potential for more
            score += potential_weight*(6-round)
    
    score += random.gauss(0, 2) #a little bit of randomization never hurt anyone
    return score
