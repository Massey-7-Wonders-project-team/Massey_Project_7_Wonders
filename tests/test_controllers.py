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
