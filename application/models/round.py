from index import db
from .card import Card
from .player import Player


class Round(db.Model):
    __tablename__ = 'round'
    age = db.Column(db.Integer, default=1, primary_key=True)
    round = db.Column(db.Integer, default=1, primary_key=True)
    userId = db.Column(db.Integer, primary_key=True)
    gameId = db.Column(db.Integer, primary_key=True)
    cardName = db.Column(db.String(50), primary_key=True)
    cardNoPlayers = db.Column(db.Integer, primary_key=True)
    __table_args__ = (db.ForeignKeyConstraint([cardName, cardNoPlayers], [Card.name, Card.noPlayers]),
                      db.ForeignKeyConstraint([userId, gameId], [Player.userId, Player.gameId]), {})

