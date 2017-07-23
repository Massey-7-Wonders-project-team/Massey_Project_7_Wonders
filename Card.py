class Card:
  # Constrains properties cards can possess
  # All cards need a name, age, players, type (colour)
  def __init__ (self, name, age, players, type):
    self.name = name
    self.age = age
    self.players = players
    self.type = type
    self.picture = "" # Future proofing for later UI purposes
    
    # Costs - split into money (decreases money reserves) and materials (no decrease, only check for availability)
    self.costMoney = 0
    self.costMaterial = [0] * 7 # [Wood, Brick, Ore, Stone, Glass, Paper, Cloth]
    
    # Benefits
    self.benefits = [0] * 10 # [Points, Military, Money, Wood, Brick, Ore, Stone, Glass, Paper, Cloth]
    
    # Bonuses <- Future implementation
    
    
    # List info from player class
    # self.state = [0, 0, 3, 0, 0, 0, 0, 0, 0, 0] # [Points, Military, Money, Wood, Brick, Ore, Stone, Glass, Paper, Cloth]
    # Card counters <- I believe this makes dealing with the effects of more complex cards easier
    # self.cards = [0] * 10 # [yellow/commerce, brown/resource, blue/architecture, purple/guild, red/military, grey/advanced resources, 
                            #  green cog, green tablet, green compass, green wildcard]

  def PopulateCards (self):
    cards = []
    
    cards.append(new Card("Lumber Yard", 1, 3, [0,1,0,0,0,0,0,0,0,0]))
    cards[0].benefits[3] = 1
    
    cards.append(new Card("Ore Vein", 1, 3, [0,1,0,0,0,0,0,0,0,0]))
    cards[1].benefits[5] = 1
    
    cards.append(new Card("Clay Pool", 1, 3, [0,1,0,0,0,0,0,0,0,0]))
    cards[2].benefits[4] = 1
    
    cards.append(new Card("Stone Pit", 1, 3, [0,1,0,0,0,0,0,0,0,0]))
    cards[3].benefits[6] = 1
    
    cards.append(new Card("Loom", 1, 3, [0,0,0,0,0,1,0,0,0,0]))
    cards[4].benefits[9] = 1
    
    cards.append(new Card("Glassworks", 1, 3, [0,0,0,0,0,1,0,0,0,0]))
    cards[5].benefits[7] = 1
    
    cards.append(new Card("Press", 1, 3, [0,0,0,0,0,1,0,0,0,0]))
    cards[6].benefits[8] = 1
    
    cards.append(new Card("Altar", 1, 3, [0,0,1,0,0,0,0,0,0,0]))
    cards[7].benefits[0] = 2
    
    cards.append(new Card("Theatre", 1, 3, [0,0,1,0,0,0,0,0,0,0]))
    cards[8].benefits[0] = 2
    
    cards.append(new Card("Baths", 1, 3, [0,0,1,0,0,0,0,0,0,0]))
    cards[9].costMaterial[3] = 1
    cards[9].benefits[0] = 3
    
    cards.append(new Card("Stockade", 1, 3, [0,0,0,0,1,0,0,0,0,0]))
    cards[10].costMaterial[0] = 1
    cards[10].benefits[1] = 1
    
    cards.append(new Card("Barracks", 1, 3, [0,0,0,0,1,0,0,0,0,0]))
    cards[11].costMaterial[2] = 1
    cards[11].benefits[1] = 1
    
    cards.append(new Card("Guard Tower", 1, 3, [0,0,0,0,1,0,0,0,0,0]))
    cards[12].costMaterial[1] = 1
    cards[12].benefits[1] = 1
