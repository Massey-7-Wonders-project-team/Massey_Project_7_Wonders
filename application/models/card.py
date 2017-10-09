from index import db


class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), default='')
    noPlayers = db.Column(db.Integer, default=0)
    age = db.Column(db.Integer, default=0)
    colour = db.Column(db.String(10), default='')

    costMoney = db.Column(db.Integer, default=0)
    costWood = db.Column(db.Integer, default=0)
    costBrick = db.Column(db.Integer, default=0)
    costOre = db.Column(db.Integer, default=0)
    costStone = db.Column(db.Integer, default=0)
    costGlass = db.Column(db.Integer, default=0)
    costPaper = db.Column(db.Integer, default=0)
    costCloth = db.Column(db.Integer, default=0)
    prerequisite1 = db.Column(db.String(50), default='')
    prerequisite2 = db.Column(db.String(50), default='')

    giveWood = db.Column(db.Integer, default=0)
    giveBrick = db.Column(db.Integer, default=0)
    giveOre = db.Column(db.Integer, default=0)
    giveStone = db.Column(db.Integer, default=0)
    giveGlass = db.Column(db.Integer, default=0)
    givePaper = db.Column(db.Integer, default=0)
    giveCloth = db.Column(db.Integer, default=0)
    resourceAlternating = db.Column(db.Boolean, default=False)
    givePoints = db.Column(db.Integer, default=0)
    giveMilitary = db.Column(db.Integer, default=0)
    giveMoney = db.Column(db.Integer, default=0)
    giveResearch = db.Column(db.String(10), default='')

    def __init__(self, name, noPlayers, age, colour):
        self.name = name
        self.noPlayers = noPlayers
        self.age = age
        self.colour = colour

    def __eq__(self, other):
        if type(self) is type(other):
            return self.id == other.id
        else:
            return False

    def serialise(self):
        return {
            'id': self.id,
            'name': self.name,
            'noPlayers': self.noPlayers,
            'age': self.age,
            'colour': self.colour,
            'costMoney': self.costMoney,
            'costWood': self.costWood,
            'costBrick': self.costBrick,
            'costOre': self.costOre,
            'costStone': self.costStone,
            'costGlass': self.costGlass,
            'costPaper': self.costPaper,
            'costCloth': self.costCloth,
            'prerequisite1': self.prerequisite1,
            'prerequisite2': self.prerequisite2,
            'giveWood': self.giveWood,
            'giveBrick': self.giveBrick,
            'giveOre': self.giveOre,
            'giveStone': self.giveStone,
            'giveGlass': self.giveGlass,
            'givePaper': self.givePaper,
            'giveCloth': self.giveCloth,
            'resourceAlternating': self.resourceAlternating,
            'givePoints': self.givePoints,
            'giveMilitary': self.giveMilitary,
            'giveMoney': self.giveMoney,
            'giveResearch': self.giveResearch
        }
