class Player: 
  # This class tracks a player's state throughout the game
  def __init__ (self, name, position):
    self.name = name #necessary?
    self.position = position #order in which created, used for determining neighbours 
    self.money = 3
    self.points = 0
    self.military = 0
    self.played = [] # To add played cards into
    # Materials
    self.wood = 0
    self.brick = 0
    self.stone = 0
    self.ore = 0
    self.glass = 0
    self.cloth = 0
    self.paper = 0
    # Green Research Cards
    self.cog = 0
    self.tablet = 0
    self.compass = 0
    self.wildcard = 0
    # Other card counters <- I believe this makes dealing with the effects of more complex cards easier
    self.yellowCard = 0 #commerce
    self.brownCard = 0 #basic resource
    self.blueCard = 0 #architecture
    self.purpleCard = 0 #guild
    self.redCard = 0 #military
    self.greenCard = 0 #research
    self.greyCard = 0 #advanced resource
  
  # hands - do players hold hands, or are hands assigned to players? Probably the second is a faster implementation?
