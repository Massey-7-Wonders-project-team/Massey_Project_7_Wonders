from index import db
from .card import Card


class Round(db.Model):
    __tablename__ = 'round'
    age = db.Column(db.Integer, default=1, primary_key=True)
    round = db.Column(db.Integer, default=1, primary_key=True)
    playerId = db.Column(db.Integer, db.ForeignKey('player.id'))
    cardName = db.Column(db.String(50), db.ForeignKey('card.name')) #, db.ForeignKey('card.name')
    cardNoPlayers = db.Column(db.Integer, db.ForeignKey('card.noPlayers')) #, db.ForeignKey('card.noPlayers')
    card = db.relationship(Card)

