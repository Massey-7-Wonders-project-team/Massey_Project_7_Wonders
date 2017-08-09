from index import db


class Hand(db.Model):
    __tablename__ = 'hand'
    handId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    gameId = db.Column(db.Integer, db.ForeignKey('game.id'))
    moveSubmitted = db.Column(db.Boolean, default=False)
    card = db.relationship('Card', backref='card', lazy='dynamic')

