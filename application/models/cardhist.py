from index import db
from .player import Player
from .card import Card


class Cardhist(db.Model):
    __tablename__ = 'cardhist'
    id = db.Column(db.Integer, primary_key=True)
    playerId = db.Column(db.Integer, db.ForeignKey('player.id'))
    cardId = db.Column(db.Integer, db.ForeignKey('card.id'))
    card_name = db.Column(db.String(30), default='')
    card_colour = db.Column(db.String(30), default='')
    discarded = db.Column(db.Boolean, default=False)
    for_wonder = db.Column(db.Boolean, default=False)

    def serialise(self):
        return {
            'playerId':self.playerId,
            'card_name':self.card_name,
            'card_colour':self.card_colour
        }
