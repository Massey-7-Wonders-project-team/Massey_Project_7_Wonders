class Player: 
  # This class tracks a player's state throughout the game
  def __init__ (self, name, position):
    self.name = name #necessary?
    self.position = position #order in which created, used for determining neighbours 
    self.state = [0, 0, 3, 0, 0, 0, 0, 0, 0, 0] # [Points, Military, Money, Wood, Brick, Ore, Stone, Glass, Paper, Cloth]

    # Card counters <- I believe this makes dealing with the effects of more complex cards easier
    self.cards = [0] * 10 # [yellow/commerce, brown/resource, blue/architecture, purple/guild, red/military, grey/advanced resources, 
                          #  green cog, green tablet, green compass, green wildcard]
  
  # hands - do players hold hands, or are hands assigned to players? Probably the second is a faster implementation?
