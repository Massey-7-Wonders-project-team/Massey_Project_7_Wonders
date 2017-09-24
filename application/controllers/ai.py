from .database_functions import *

def rank_move(player, card):
    """ 
    Future method to rank card scores - not currently used
    """
    score = 0

    # Gather resources
    score += card.giveGlass * 10 + card.givePaper * 10 + card.giveCloth * 10
    score += card.giveWood * 5 + card.giveBrick * 5 + card.giveStone * 5 + card.giveOre * 5

    # Penalties if player already has a lot

    # Score
    score += card.givePoints * 3

    # Military - extra points if military is close between neighbours

    # Add bonuses if resources needed for wonder -- TODO
    wonder_cards = get_all_wonder_cards(player)

    # Add bonus for lots of research cards

    # Yellow/purple card treatment
