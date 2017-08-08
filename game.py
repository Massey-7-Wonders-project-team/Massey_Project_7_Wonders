from index import db
import random


class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer(), primary_key=True)
    player = db.relationship('User', backref='scenario', lazy='dynamic')
    discarded = db.relationship('Card')

    def checkMove(self, card, player):
        if player.state['money'] < card.costMoney:
            return False
        for key in card.requiresMaterial:
            if player.state[key] < card.requiresMaterial[key]:
                return False
        return True

    # RELIES ON CHECK MOVE VALIDATION BEFORE CALL
    def playCard(self, card):
        self.player.cards.append(card)
        for key in card.benefits:
            self.player.state[key] += card.benefits[key]
        self.player.state['money'] -= card.costMoney

    def discardCard(self, card):
        self.discarded.append(card)
        self.player.money += 3

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
