from testing_config import BaseTestConfig
from flask_testing import TestCase
from application.controllers.database_functions import *
from manage import *
from index import app

"""
def no_nones(object):
    if not [p for p in [field for field in dir(object) if not field.startswith('__')] if not p]:
        return True
    else:
        return False


class TestModels(BaseTestConfig):
    def test_get_user_with_email_and_password(self):
        self.assertTrue(
                User.get_user_with_email_and_password(
                        self.default_user["email"],
                        self.default_user["password"])
        )


class Defaults():
    default_user = User(email='a@a.com', name='test', password='testcase')
    default_user2 = User(email='b@b.com', name='test', password='testcase')
    default_game = Game()
    default_player = Player(userId=default_user.id, gameId=default_game.id, name=default_user.name)
    default_player2 = Player(userId=default_user2.id, gameId=default_game.id, name=default_user2.name)
    default_card = Card('test', 3, 1, 'brown')


class TestModelsWithAlchemy(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_game(self):
        game = Game()

        db_committing_function(game)
        gameDB = get_game(game.id)

        self.assertTrue(
            game.serialise() == gameDB.serialise()
        )

    def test_game_serialise(self):
        db_committing_function(Defaults.default_game)
        dict = Defaults.default_game.serialise()

        self.assertTrue(
            dict.get('id') == 1 and
            dict.get('age') == 0 and
            dict.get('round') == 1 and
            dict.get('started') is False and
            dict.get('complete') is False and
            dict.get('single_player') is False
        )

    def test_player(self):
        user = Defaults.default_user
        game = Defaults.default_game
        player = Player(userId=user.id, gameId=game.id, name=user.name)

        db_committing_function(user, game, player)
        playerDB = get_player(player.id)

        #print(player.serialise())
        #self.assertTrue(False)

        # Checks Alchemy has created the object and filled in all fields
        self.assertTrue(no_nones(playerDB))

    def test_player_serialise(self):
        user = User(email='c@c.com', name='test', password='testcase')
        game = Game()
        db_committing_function(user, game)

        player = Player(userId=user.id, gameId=game.id, name=user.name)
        db_committing_function(player)

        dict = player.serialise()

        self.assertTrue(
            dict.get('id') == 1 and
            dict.get('gameId') == 1 and
            dict.get('userId') == 1 and
            dict.get('ready') is False and
            dict.get('profile') == player.name and
            dict.get('ai') is False and
            dict.get('left_id') is None and
            dict.get('right_id') is None and
            dict.get('wonder') == '' and
            dict.get('wonder_level') == 0 and
            dict.get('max_wonder') == 0 and
            dict.get('wood') == 0 and
            dict.get('brick') == 0 and
            dict.get('stone') == 0 and
            dict.get('ore') == 0 and
            dict.get('glass') == 0 and
            dict.get('paper') == 0 and
            dict.get('cloth') == 0 and
            dict.get('points') == 0 and
            dict.get('military') == 0 and
            dict.get('money') == 3 and
            dict.get('cog') == 0 and
            dict.get('tablet') == 0 and
            dict.get('compass') == 0 and
            dict.get('wildcard') == 0 and
            dict.get('military_loss') == 0 and
            dict.get('extra_wood') == 0 and
            dict.get('extra_brick') == 0 and
            dict.get('extra_stone') == 0 and
            dict.get('extra_ore') == 0 and
            dict.get('extra_glass') == 0 and
            dict.get('extra_paper') == 0 and
            dict.get('extra_cloth') == 0
        )

    def test_player_equality(self):
        user = Defaults.default_user
        user2 = Defaults.default_user2
        game = Defaults.default_game
        db_committing_function(user, user2, game)

        different_player = Defaults.default_player2
        db_committing_function(Defaults.default_player, Defaults.default_player2)
        same_player = get_player(Defaults.default_player.id)

        self.assertTrue(same_player == Defaults.default_player)
        self.assertFalse(different_player == Defaults.default_player)

    def test_card(self):
        card = Card('test', 3, 1, 'brown')

        db_committing_function(card)
        cardDB = get_card(card.id)

        self.assertTrue(no_nones(cardDB))

    def test_card_equality(self):
        card = Card('test', 3, 1, 'brown')
        card2 = Card('test', 3, 1, 'brown')

        db_committing_function(card, card2)
        cardDB = get_card(card.id)

        self.assertTrue(
            card == cardDB and
            card != card2
        )

    def test_card_serialise(self):
        card = Card('test', 3, 1, 'brown')
        db_committing_function(card)

        dict = card.serialise()

        self.assertTrue(
            dict.get('id') == 1 and
            dict.get('name') == card.name and
            dict.get('noPlayers') == card.noPlayers and
            dict.get('age') == card.age and
            dict.get('colour') == card.colour and
            dict.get('costWood') == 0 and
            dict.get('costBrick') == 0 and
            dict.get('costStone') == 0 and
            dict.get('costOre') == 0 and
            dict.get('costGlass') == 0 and
            dict.get('costPaper') == 0 and
            dict.get('costCloth') == 0 and
            dict.get('costMoney') == 0 and
            dict.get('resourceAlternating') is False and
            dict.get('prerequisite1') == '' and
            dict.get('prerequisite2') == '' and
            dict.get('givePoints') == 0 and
            dict.get('giveMilitary') == 0 and
            dict.get('giveMoney') == 0 and
            dict.get('giveResearch') == '' and
            dict.get('giveWood') == 0 and
            dict.get('giveBrick') == 0 and
            dict.get('giveStone') == 0 and
            dict.get('giveOre') == 0 and
            dict.get('giveGlass') == 0 and
            dict.get('givePaper') == 0 and
            dict.get('giveCloth') == 0
        )

    def test_round(self):
        card = Card('test', 3, 1, 'brown')
        user = User(email='d@d.com', name='test', password='testcase')
        game = Game()
        db_committing_function(card, user, game)
        player = Player(userId=user.id, gameId=game.id, name=user.name)
        db_committing_function(player)
        round = Round(cardId=card.id, playerId=player.id)
        db_committing_function(round)

        self.assertTrue(
            round.id == 1 and
            round.age == 1 and
            round.round == 1 and
            round.playerId == player.id and
            round.cardId == card.id
        )

    def test_round_serialise(self):
        card = Card('test', 3, 1, 'brown')
        user = User(email='d@d.com', name='test', password='testcase')
        game = Game()
        db_committing_function(card, user, game)
        player = Player(userId=user.id, gameId=game.id, name=user.name)
        db_committing_function(player)
        round = Round(cardId=card.id, playerId=player.id)
        db_committing_function(round)

        dict = round.serialise()
        print(dict)

        self.assertTrue(
            dict.get('id') == 1 and
            dict.get('age') == 1 and
            dict.get('round') == 1 and
            dict.get('player') == player.id and
            dict.get('card') == card.serialise()
        )

    def test_cardhist(self):
        card = Card('test', 3, 1, 'brown')
        user = User(email='d@d.com', name='test', password='testcase')
        game = Game()
        db_committing_function(card, user, game)
        player = Player(userId=user.id, gameId=game.id, name=user.name)
        db_committing_function(player)
        cardhist = Cardhist(cardId=card.id, card_name=card.name, playerId=player.id, card_colour=card.colour)
        db_committing_function(cardhist)

        self.assertTrue(
            cardhist.id == 1 and
            cardhist.discarded is False and
            cardhist.for_wonder is False and
            cardhist.playerId == player.id and
            cardhist.cardId == card.id and
            cardhist.card_name == card.name and
            cardhist.card_colour == card.colour
        )

    def test_cardhist_serialise(self):
        card = Card('test', 3, 1, 'brown')
        user = User(email='d@d.com', name='test', password='testcase')
        game = Game()
        db_committing_function(card, user, game)
        player = Player(userId=user.id, gameId=game.id, name=user.name)
        db_committing_function(player)
        cardhist = Cardhist(cardId=card.id, card_name=card.name, playerId=player.id, card_colour=card.colour)
        db_committing_function(cardhist)

        dict = cardhist.serialise()

        self.assertEqual(dict.get('playerId'), player.id)
        self.assertEqual(dict.get('card_name'), card.name)
        self.assertEqual(dict.get('card_colour'), card.colour)

    def test_wonder(self):
        wonder = Wonder()
        db_committing_function(wonder)

        self.assertTrue(
            wonder.id == 1 and
            wonder.slots == 0 and
            wonder.card_4 == '' and
            wonder.card_3 == '' and
            wonder.card_2 == '' and
            wonder.card_1 == '' and
            wonder.card_0 == '' and
            wonder.name == ''
        )

    def test_wonder_serialise(self):
        wonder = Wonder()
        db_committing_function(wonder)

        dict = wonder.serialise()

        self.assertTrue(
            dict.get('id') == 1 and
            dict.get('slots') == 0 and
            dict.get('card_4') == '' and
            dict.get('card_3') == '' and
            dict.get('card_2') == '' and
            dict.get('card_1') == '' and
            dict.get('card_0') == '' and
            dict.get('name') == ''
        )
"""
