class Game:
    def __init__(self):
        discarded = []

    def checkMove(self, card, player):
        if player.state['money'] < card.costMoney:
            return False
        for key in card.requiresMaterial:
            if player.state[key] < card.requiresMaterial[key]:
                return False
        return True

    # RELIES ON CHECK MOVE VALIDATION BEFORE CALL
    def playCard(self, card, player):
        player.cards.append(card)
        for key in card.benefits:
            player.state[key] += card.benefits[key]
        player.state['money'] -= card.costMoney
        return player

    def discardCard(self, card, player):
        self.discarded.append(card)
        player.state['money'] += 3
