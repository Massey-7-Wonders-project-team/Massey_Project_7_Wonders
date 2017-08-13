from index import db
from .player import Player
from .card import Card


class Cardhist(db.Model):
    __tablename__ = 'cardhist'
    playerId = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    cardId = db.Column(db.Integer, db.ForeignKey('card.id'), primary_key=True)
    discarded = db.Column(db.Boolean, default=False)
