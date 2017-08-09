from index import db


class Card(db.Model):
    __tablename__ = 'card'
    name = db.Column(db.String(50), primary_key=True)
    noPlayers = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    type = db.Column(db.String(10))
    hand = db.relationship('Hand', backref='hand', lazy='dynamic')

    costMoney = db.Column(db.Integer)
    costWood = db.Column(db.Integer)
    costBrick = db.Column(db.Integer)
    costOre = db.Column(db.Integer)
    costStone = db.Column(db.Integer)
    costGlass = db.Column(db.Integer)
    costPaper = db.Column(db.Integer)
    costCloth = db.Column(db.Integer)

    giveWood = db.Column(db.Integer)
    giveBrick = db.Column(db.Integer)
    giveOre = db.Column(db.Integer)
    giveStone = db.Column(db.Integer)
    giveGlass = db.Column(db.Integer)
    givePaper = db.Column(db.Integer)
    giveCloth = db.Column(db.Integer)
    givePoints = db.Column(db.Integer)
    giveMilitary = db.Column(db.Integer)
    giveMoney = db.Column(db.Integer)
