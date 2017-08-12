from index import db
from .card import Card
from .player import Player


class Round(db.Model):
    __tablename__ = 'round'
    age = db.Column(db.Integer, default=1, primary_key=True)
    round = db.Column(db.Integer, default=1, primary_key=True)
    playerId = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    cardId = db.Column(db.Integer, db.ForeignKey('card.id'), primary_key=True)

