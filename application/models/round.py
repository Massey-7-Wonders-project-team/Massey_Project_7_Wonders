from index import db
from .card import Card
from .player import Player


class Round(db.Model):
    __tablename__ = 'round'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, default=1)
    round = db.Column(db.Integer, default=1)
    playerId = db.Column(db.Integer, db.ForeignKey('player.id'))
    cardId = db.Column(db.Integer, db.ForeignKey('card.id'))

    def serialise(self):
        return {
            'id': self.id,
            'age': self.age,
            'round': self.round,
            'card': Card.serialise(Card.query.filter_by(id=self.cardId).first())
        }
