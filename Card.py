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

  def PopulateCards (self):
    cards = []
    
    cards.append(new Card("Lumber Yard", 1, 3, "brown"))
    cards[0].benefits[3] = 1
    
    cards.append(new Card("Ore Vein", 1, 3, "brown"))
    cards[1].benefits[5] = 1
    
    cards.append(new Card("Clay Pool", 1, 3, "brown"))
    cards[2].benefits[4] = 1
    
    cards.append(new Card("Stone Pit", 1, 3, "brown"))
    cards[3].benefits[6] = 1
