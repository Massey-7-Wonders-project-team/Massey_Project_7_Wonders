from index import db
from .player import Player
from .card import Card


class Cardhist(db.Model):
    __tablename__ = 'cardhist'
    id = db.Column(db.Integer, primary_key=True)
    playerId = db.Column(db.Integer, db.ForeignKey('player.id'))
    cardId = db.Column(db.Integer, db.ForeignKey('card.id'))
    discarded = db.Column(db.Boolean, default=False)
