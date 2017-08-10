from index import db


class Card(db.Model):
    __tablename__ = 'card'
    name = db.Column(db.String(50), primary_key=True)
    noPlayers = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, default=1)
    type = db.Column(db.String(10))

    costMoney = db.Column(db.Integer, default=0)
    costWood = db.Column(db.Integer, default=0)
    costBrick = db.Column(db.Integer, default=0)
    costOre = db.Column(db.Integer, default=0)
    costStone = db.Column(db.Integer, default=0)
    costGlass = db.Column(db.Integer, default=0)
    costPaper = db.Column(db.Integer, default=0)
    costCloth = db.Column(db.Integer, default=0)

    giveWood = db.Column(db.Integer, default=0)
    giveBrick = db.Column(db.Integer, default=0)
    giveOre = db.Column(db.Integer, default=0)
    giveStone = db.Column(db.Integer, default=0)
    giveGlass = db.Column(db.Integer, default=0)
    givePaper = db.Column(db.Integer, default=0)
    giveCloth = db.Column(db.Integer, default=0)
    givePoints = db.Column(db.Integer, default=0)
    giveMilitary = db.Column(db.Integer, default=0)
    giveMoney = db.Column(db.Integer, default=0)
