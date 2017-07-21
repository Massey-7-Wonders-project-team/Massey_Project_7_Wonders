class Card:
  # Constrains properties cards can possess
  # All cards need a name, age, players, type (colour)
  def __init__ (self, name, age, players, type):
    self.name = name
    self.age = age
    self.players = players
    self.type = type
    self.picture = "" # Future proofing for later UI purposes
    
    # Costs
    self.costMoney = 0
    self.costWood = 0
    self.costBrick = 0
    self.costOre = 0
    self.costStone = 0
    self.costGlass = 0
    self.costPaper = 0
    self.costCloth = 0
    
    # Benefits
    self.givesPoints = 0
    self.givesMilitary = 0
    self.givesMoney = 0
    self.givesWood = 0
    self.givesBrick = 0
    self.givesOre = 0
    self.givesStone = 0
    self.givesGlass = 0
    self.givesCloth = 0
    self.givesPaper = 0
    
    # Bonuses <- Future implementation
