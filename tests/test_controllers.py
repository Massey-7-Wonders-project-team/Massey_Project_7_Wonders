from testing_config import BaseTestConfig
from flask_testing import TestCase
from application.controllers.database_functions import *
from application.controllers.card_logic import *
from manage import *
from index import app

class TestControllersWithAlchemy(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    #test process_card
    def test_process_card_not_in_hand(self):
        game = Game(age=1, round=1)
        user = User(email='a@a.com', name='test', password='testcase')
        card = Card('test', 3, 1, 'brown')
        db_committing_function(user,game,card)
        player = Player(userId=user.id, gameId=game.id, name=user.name)
        db_committing_function(player)
        
        self.assertFalse(process_card(card,player,False,False))

    def test_process_card_single_card(self):
        game = Game(age=1, round=1)
        user = User(email='a@a.com', name='test', password='testcase')
        card = Card('test', 3, 1, 'brown')
        db_committing_function(user,game,card)
        player = Player(userId=user.id, gameId=game.id, name=user.name)
        db_committing_function(player)
        round = Round(cardId=card.id, playerId=player.id)
        db_committing_function(round)
        
        self.assertTrue(process_card(card,player,False,False))
    
    def test_process_card_no_repeats(self):
        game = Game(age=1, round=1)
        user = User(email='a@a.com', name='test', password='testcase')
        card = Card('test', 3, 1, 'brown')
        card2 = Card('test', 3, 1, 'brown')
        db_committing_function(user,game,card,card2)
        player = Player(userId=user.id, gameId=game.id, name=user.name)
        db_committing_function(player)
        round = Round(cardId=card.id, playerId=player.id)
        round2 = Round(cardId=card2.id, playerId=player.id, round=2)
        db_committing_function(round,round2)
        
        process_card(card,player,False,False)
        
        self.assertFalse(process_card(card2,player,False,False))
        
    def test_process_card_different_cards(self):
        game = Game(age=1, round=1)
        user = User(email='a@a.com', name='test', password='testcase')
        card = Card('test', 3, 1, 'brown')
        card2 = Card('second_test', 3, 1, 'brown')
        db_committing_function(user,game,card,card2)
        player = Player(userId=user.id, gameId=game.id, name=user.name)
        db_committing_function(player)
        round = Round(cardId=card.id, playerId=player.id)
        round2 = Round(cardId=card2.id, playerId=player.id, round=2)
        db_committing_function(round,round2)
        
        process_card(card,player,False,False)
        
        self.assertTrue(process_card(card2,player,False,False))
        
    def test_process_card_with_resource_cost(self):
        game = Game(age=1, round=1)
        user = User(email='a@a.com', name='test', password='testcase')
        
        lumberYard = Card('Lumber Yard', 3, 1, 'brown')
        lumberYard.set_benefit_wood(1)
        baths = Card('Baths', 3, 1, 'blue')
        baths.set_cost_stone(1)
        baths.set_benefit_points(3)
        stockade = Card('Stockade', 3, 1, 'red')
        stockade.set_cost_wood(1)
        stockade.set_benefit_military(1)
        
        db_committing_function(user,game,lumberYard,baths,stockade)
        player = Player(userId=user.id, gameId=game.id, name=user.name)
        db_committing_function(player)
        round = Round(cardId=lumberYard.id, playerId=player.id)
        round2a = Round(cardId=baths.id, playerId=player.id, round=2)
        round2b = Round(cardId=stockade.id, playerId=player.id, round=2)
        db_committing_function(round,round2a,round2b)
        
        process_card(lumberYard,player,False,False)
        
        #can't play this card
        previous_points = player.points
        self.assertFalse(process_card(baths,player,False,False))
        self.assertEqual(previous_points, player.points)
        
        #can play this one
        previous_military = player.military
        self.assertTrue(process_card(stockade,player,False,False))
        self.assertEqual(previous_military+1, player.military)
    
    def test_process_card_discard(self):
        game = Game(age=1, round=1)
        user = User(email='a@a.com', name='test', password='testcase')
        
        lumberYard = Card('Lumber Yard', 3, 1, 'brown')
        lumberYard.set_benefit_wood(1)
        baths = Card('Baths', 3, 1, 'blue')
        baths.set_cost_stone(1)
        baths.set_benefit_points(3)
        stockade = Card('Stockade', 3, 1, 'red')
        stockade.set_cost_wood(1)
        stockade.set_benefit_military(1)
        
        db_committing_function(user,game,lumberYard,baths,stockade)
        
        player = Player(userId=user.id, gameId=game.id, name=user.name)
        db_committing_function(player)
        round1 = Round(cardId=lumberYard.id, playerId=player.id)
        round2 = Round(cardId=baths.id, playerId=player.id, round=2)
        round3 = Round(cardId=stockade.id, playerId=player.id, round=3)
        db_committing_function(round1,round2,round3)
        
        process_card(lumberYard,player,False,False)
        
        #can play any cards regardless of whether they meet the resource cost
        previous_money = player.money
        self.assertTrue(process_card(baths,player,True,False))
        self.assertEqual(previous_money+3, player.money)
        
        round3 = Round(cardId=stockade.id, playerId=player.id, round=3)
        db_committing_function(round3)
        previous_money = player.money
        self.assertTrue(process_card(stockade,player,True,False))
        self.assertEqual(previous_money+3, player.money)
        
    def test_process_card_monetary_cost(self):
        game = Game(age=1, round=1)
        user = User(email='a@a.com', name='test', password='testcase')
        timberYard = Card('Timber Yard', 3, 1, 'brown')
        timberYard.set_benefit_wood(1)
        timberYard.set_benefit_stone(1)
        timberYard.set_resource_alternating(True)
        timberYard.set_cost_money(1)
        db_committing_function(user,game,timberYard)
        player = Player(userId=user.id, gameId=game.id, name=user.name, money=0)
        db_committing_function(player)
        round = Round(cardId=timberYard.id, playerId=player.id)
        #card_hist = Cardhist()
        db_committing_function(round)#,card_hist)
        
        self.assertEqual(0,player.money)
        self.assertFalse(process_card(timberYard,player,False,False))
        self.assertEqual(0,player.money)
        player.money = 3
        db_committing_function(player)
        self.assertTrue(process_card(timberYard,player,False,False))
        self.assertEqual(2,player.money)

    def test_trade_not_enough_goods(self):
        user = User(email='test@test.com', name='test', password='tester')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        game = Game()
        db_committing_function(user, user1, user2, game)

        players = []
        player1 = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player1)
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        card1 = Card('test', 3, 1, 'brown')
        card1.costBrick = 1
        card1.costWood = 1
        card_left = Card('test2', 3, 1, 'brown')
        card_left.resourceAlternating = True
        card_left.giveBrick = 1
        card_left.giveWood = 1
        db_committing_function(card1, card_left)

        hist = Cardhist(playerId=player1.left_id, cardId=card_left.id, card_colour=card_left.colour)
        db_committing_function(hist)
        success, trade_info = calculate_trades(card1, player1)

        self.assertFalse(success)
        self.assertTrue(trade_info is None)

    def test_trade_no_trade_needed(self):
        user = User(email='test@test.com', name='test', password='tester')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        game = Game()
        db_committing_function(user, user1, user2, game)

        players = []
        player1 = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player1)
        player1.wood = 1
        player1.brick = 1
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        card1 = Card('test', 3, 1, 'brown')
        card1.costBrick = 1
        card1.costWood = 1
        db_committing_function(card1)

        success, trade_info = calculate_trades(card1, player1)

        self.assertTrue(success)
        self.assertTrue(trade_info is None)

    def test_trade_trade_needed(self):
        user = User(email='test@test.com', name='test', password='tester')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        game = Game()
        db_committing_function(user, user1, user2, game)

        players = []
        player1 = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player1)
        player1.wood = 1
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        card1 = Card('test', 3, 1, 'brown')
        card1.costBrick = 1
        card1.costWood = 1
        card_left = Card('test2', 3, 1, 'brown')
        card_left.resourceAlternating = True
        card_left.giveBrick = 1
        card_left.giveWood = 1
        db_committing_function(card1, card_left)

        hist = Cardhist(playerId=player1.left_id, cardId=card_left.id, card_colour=card_left.colour)
        db_committing_function(hist)
        success, trade_info = calculate_trades(card1, player1)

        self.assertTrue(success)
        self.assertTrue(
            sum(trade_info['left']) == 1 and
            trade_info['left_cost'] == 2 and
            trade_info['total_cost'] == 2 and
            trade_info['possible'] is True
        )
