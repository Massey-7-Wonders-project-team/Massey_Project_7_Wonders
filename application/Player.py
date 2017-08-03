from index import db

class Player(db.Model):
  # This class tracks a player's state throughout the game
  name = db.Column(db.String(50), primary_key=True)
  position = db.Column(db.Integer, primary_key=True)
  state = db.relationship(db.State)
  cards = db.relationship(db.Card)

  def __init__ (self, name, position):
    self.name = name #necessary?
    self.position = position #order in which created, used for determining neighbours 
    self.state = {'Points': 0,
                  'Military': 0,
                  'Money': 3,
                  'Wood': 0,
                  'Brick': 0,
                  'Ore': 0,
                  'Stone': 0,
                  'Glass': 0,
                  'Paper': 0,
                  'Cloth': 0}
    self.cards = [] # Shows which cards have already been played

class State(db.Model):
    Points = db.Column(db.Integer)
    Military = db.Column(db.Integer)
    Money = db.Column(db.Integer)
    State = db.relationship(db.Substate)

class Substate(db.Model):
    Wood = db.Column(db.Integer)
    Brick = db.Column(db.Integer)
    Ore = db.Column(db.Integer)
    Stone = db.Column(db.Integer)
    Glass = db.Column(db.Integer)
    Paper = db.Column(db.Integer)
    Cloth = db.Column(db.Integer)

class Card(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    age = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10))
    costMoney = db.Column(db.Integer)
    requiresMaterial = db.relationship(db.Substate)
    benefits = db.relationship(db.State)

    def __init__(self, name, type, age):
        self.name = name
        self.age = age
        self.type = type
        self.costMoney = 0
        self.requiresMaterial = {'Wood': 0,
                                 'Brick': 0,
                                 'Ore': 0,
                                 'Stone': 0,
                                 'Glass': 0,
                                 'Papyrus': 0,
                                 'Cloth': 0}

        self.benefits = {'Points': 0,
                         'Military': 0,
                         'Money': 0,
                         'Wood': 0,
                         'Brick': 0,
                         'Ore': 0,
                         'Stone': 0,
                         'Glass': 0,
                         'Papyrus': 0,
                         'Cloth': 0}

        # Bonuses <- Future implementation
