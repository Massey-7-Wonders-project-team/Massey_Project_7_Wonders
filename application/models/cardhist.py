from index import db
from .player import Player
from .card import Card


class Cardhist(db.Model):
    __tablename__ = 'cardhist'
    id = db.Column(db.Integer, primary_key=True)
    playerId = db.Column(db.Integer, db.ForeignKey('player.id'))
    cardId = db.Column(db.Integer, db.ForeignKey('card.id'))
    card_name = db.Column(db.String(30), default='')
    discarded = db.Column(db.Boolean, default=False)
    for_wonder = db.Column(db.Boolean, default=False)

    def serialise(self):
        return {
            'id':self.id,
            'playerId':self.playerId,
            'cardId':self.cardId,
            'card_name':self.card_name,
            'discarded':self.discarded,
            'for_wonder': self.for_wonder
        }
