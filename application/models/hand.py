from index import db

'''
class Hand(db.Model):
    __tablename__ = 'hand'
    handId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    gameId = db.Column(db.Integer, db.ForeignKey('game.id'))

    card = db.relationship('Card', backref='card', lazy='dynamic')

    def dealAge(self, age):
        db.session.session_factory
        hands = []
        for player in self.player:
            hand = []
            for card in range(7):  # Each loop takes a random card and adds it to the hand
                cardInfo = table.pop(random.random(len(table)))
                hand.append(Card(cardInfo[0], cardInfo[1], cardInfo[2]))
                # Include other information about costs and benefits
            hands.append(hand)
        return hands
'''
