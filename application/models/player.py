from index import db


class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer(), primary_key=True)
    gameId = db.Column(db.Integer, db.ForeignKey('game.id'))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))

    wood = db.Column(db.Integer, default=0)
    brick = db.Column(db.Integer, default=0)
    ore = db.Column(db.Integer, default=0)
    stone = db.Column(db.Integer, default=0)
    glass = db.Column(db.Integer, default=0)
    paper = db.Column(db.Integer, default=0)
    cloth = db.Column(db.Integer, default=0)
    points = db.Column(db.Integer, default=0)
    military = db.Column(db.Integer, default=0)
    money = db.Column(db.Integer, default=3)
