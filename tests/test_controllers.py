from testing_config import BaseTestConfig
from flask_testing import TestCase
from application.controllers.database_functions import *
from application.controllers.card_logic import *
from application.controllers.game_state_functions import *
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
        user = User(email='test@test.com', name='test', password='tester')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        game = Game(age=1)
        card = Card('test', 3, 1, 'brown')
        db_committing_function(user, user1, user2, game, card)

        players = []
        player1 = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player1)
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        stats = process_card(card,player1,False,False)
        self.assertFalse(stats['possible'])
        self.assertTrue(stats['message'] == 'test is not part of this hand')

    def test_process_card_single_card(self):
        user = User(email='test@test.com', name='test', password='tester')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        game = Game(age=1)
        card = Card('test', 3, 1, 'brown')
        db_committing_function(user, user1, user2, game, card)

        players = []
        player1 = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player1)
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        round = Round(cardId=card.id, playerId=player1.id)
        db_committing_function(round)

        stats = process_card(card,player1,False,False)
        self.assertTrue(stats['possible'])
    
    def test_process_card_no_repeats(self):
        user = User(email='test@test.com', name='test', password='tester')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        game = Game(age=1)
        card = Card('test', 3, 1, 'brown')
        card2 = Card('test', 3, 1, 'brown')
        db_committing_function(user, user1, user2, game, card, card2)

        players = []
        player1 = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player1)
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        round = Round(cardId=card.id, playerId=player1.id)
        round2 = Round(cardId=card2.id, playerId=player1.id, round=2)
        db_committing_function(round, round2)

        _ = process_card(card, player1, False, False)
        game.round = 2
        db_committing_function(game)

        stats = process_card(card2, player1, False, False)
        self.assertFalse(stats['possible'])
        self.assertTrue(stats['message'] == 'You already have a test card. Only one of each type may be played')
        
    def test_process_card_different_cards(self):
        user = User(email='test@test.com', name='test', password='tester')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        game = Game(age=1)
        card = Card('test', 3, 1, 'brown')
        card2 = Card('second_test', 3, 1, 'brown')
        db_committing_function(user, user1, user2, game, card, card2)

        players = []
        player1 = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player1)
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        round = Round(cardId=card.id, playerId=player1.id)
        round2 = Round(cardId=card2.id, playerId=player1.id, round=2)
        db_committing_function(round, round2)

        _ = process_card(card, player1, False, False)
        game.round = 2
        db_committing_function(game)

        stats = process_card(card2, player1, False, False)
        print(stats)
        self.assertTrue(stats['possible'])
        self.assertTrue(stats['message'] == 'second_test successfully played')
        
    def test_process_card_with_resource_cost(self):
        game = Game(age=1, round=1)
        user = User(email='a@a.com', name='test', password='testcase')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        
        baths = Card('Baths', 3, 1, 'blue')
        baths.costStone = 1
        baths.givePoints = 3
        stockade = Card('Stockade', 3, 1, 'red')
        stockade.costWood = 1
        stockade.giveMilitary = 1
        timber = Card('Forest', 3, 1, 'brown')
        timber.giveWood = 1
        db_committing_function(user,game,baths,stockade,timber)

        players = []
        player1 = Player(gameId=game.id, userId=user.id, name=user.name)
        player1.wood = 1
        players.append(player1)
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        ch = Cardhist(cardId=timber.id, playerId=player1.id)
        round2a = Round(cardId=baths.id, playerId=player1.id)
        round2b = Round(cardId=stockade.id, playerId=player1.id)
        db_committing_function(round2a,round2b,ch)

        #can't play this card
        previous_points = player1.points
        stats = process_card(baths,player1,False,False)
        self.assertFalse(stats['possible'])
        self.assertTrue(stats['message'] == "The necessary resources are not available in your or your neighbours' civilisations")
        self.assertEqual(previous_points, player1.points)
        
        #can play this one
        previous_military = player1.military
        stats = process_card(stockade, player1, False, False)
        self.assertTrue(stats['possible'])
        self.assertEqual(previous_military+1, player1.military)
    
    def test_process_card_discard(self):
        game = Game(age=1, round=1)
        user = User(email='a@a.com', name='test', password='testcase')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        
        lumberYard = Card('Lumber Yard', 3, 1, 'brown')
        lumberYard.giveWood = 1
        baths = Card('Baths', 3, 1, 'blue')
        baths.costStone = 1
        baths.givePoints = 3
        stockade = Card('Stockade', 3, 1, 'red')
        stockade.costWood = 1
        stockade.giveMilitary = 1
        
        db_committing_function(user,game,lumberYard,baths,stockade, user1, user2)

        players = []
        player = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player)
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        round1 = Round(cardId=lumberYard.id, playerId=player.id)
        round2 = Round(cardId=baths.id, playerId=player.id, round=2)
        round3 = Round(cardId=stockade.id, playerId=player.id, round=3)
        db_committing_function(round1,round2,round3)
        
        process_card(lumberYard,player,False,False)
        
        #can play any cards regardless of whether they meet the resource cost
        previous_money = player.money
        game.round = 2
        db_committing_function(game)
        self.assertTrue(process_card(baths,player,True,False)['possible'])
        self.assertEqual(previous_money+3, player.money)

        game.round = 3
        db_committing_function(game)
        previous_money = player.money
        self.assertTrue(process_card(stockade,player,True,False)['possible'])
        self.assertEqual(previous_money+3, player.money)
        
    def test_process_card_monetary_cost(self):
        game = Game(age=1, round=1)
        user = User(email='a@a.com', name='test', password='testcase')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        timberYard = Card('Timber Yard', 3, 1, 'brown')
        timberYard.giveWood = 1
        timberYard.giveWood = 1
        timberYard.resourceAlternating = True
        timberYard.costMoney = 1
        db_committing_function(user,game,timberYard,user1,user2)
        players = []
        player = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player)
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)
        round = Round(cardId=timberYard.id, playerId=player.id)
        db_committing_function(round)

        player.money = 0
        db_committing_function(player)
        self.assertEqual(0,player.money)
        self.assertFalse(process_card(timberYard,player,False,False)['possible'])
        self.assertEqual(0,player.money)
        player.money = 3
        db_committing_function(player)
        stats = process_card(timberYard,player,False,False)
        print(stats)
        self.assertTrue(stats['possible'])
        self.assertEqual(2,player.money)
        
    def test_process_card_prerequisites(self):
        game = Game(age=1, round=1)
        user = User(email='a@a.com', name='test', password='testcase')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')

        apothecary = Card('Apothecary', 3, 1, 'green')
        apothecary.giveResearch = 'compass'
        forum = Card('Forum', 3, 1, 'yellow')
        forum.giveCloth = 1
        forum.giveGlass = 1
        forum.givePaper = 1
        forum.resourceAlternating = True
        forum.costBrick = 2
        forum.prerequisite1 = 'East Trading Post'
        forum.prerequisite2 = 'West Trading Post'
        stables = Card('Stables', 3, 1, 'red')
        stables.giveMilitary = 2
        stables.costBrick = 1
        stables.costWood = 1
        stables.costOre = 1
        stables.prerequisite1 = 'Apothecary'
        
        db_committing_function(user,game,apothecary,forum,stables, user1,user2)
        players = []
        player = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player)
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        round1 = Round(cardId=apothecary.id, playerId=player.id)
        round2 = Round(cardId=stables.id, playerId=player.id, round=2)
        round3 = Round(cardId=forum.id, playerId=player.id, round=3)
        db_committing_function(round1, round2, round3)
        
        self.assertTrue(process_card(apothecary,player,False,False)['possible'])
        
        #can play this card
        game.round = 2
        db_committing_function(game)
        self.assertTrue(process_card(stables,player,False,False)['possible'])
        
        #can't play this card
        game.round = 3
        db_committing_function(game)
        self.assertFalse(process_card(forum,player,False,False)['possible'])
        
    def test_process_card_wonder(self):
        alex_0 = Card(name='alex_0', noPlayers=0, age=0, colour='wonder')
        alex_0.giveGlass = 1
        alex_1 = Card(name='alex_1', noPlayers=0, age=0, colour='wonder')
        alex_1.costBrick = 2
        alex_1.giveBrick = 1
        alex_1.giveOre = 1
        alex_1.giveStone = 1
        alex_1.giveWood = 1
        alex_1.resourceAlternating = True
        alex_2 = Card(name='alex_2', noPlayers=0, age=0, colour='wonder')
        alex_2.costWood = 2
        alex_2.giveGlass = 1
        alex_2.givePaper = 1
        alex_2.giveCloth = 1
        alex_2.resourceAlternating = True
        alex_3 = Card(name='alex_3', noPlayers=0, age=0, colour='wonder')
        alex_3.costStone = 3
        alex_3.givePoints = 7
        alex = Wonder(name="The Lighthouse of Alexandria", slots=3, card_0="alex_0", card_1="alex_1", card_2="alex_2", card_3="alex_3")
        db_committing_function(alex,alex_0,alex_1,alex_2,alex_3)
        
        game = Game(age=1, round=1)
        user = User(email='a@a.com', name='test', password='testcase')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        db_committing_function(user,game,user1,user2)
        players = []
        player = Player(userId=user.id, gameId=game.id, name=user.name, wonder=alex.name, max_wonder=alex.slots)
        players.append(player)
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)
        
        deal_wonders([player])
        self.assertEqual(player.wonder, alex.name)
        self.assertEqual(player.max_wonder, alex.slots)
        self.assertEqual(player.glass, 1)
        
        #first wonder
        card1 = Card('test', 3, 1, 'brown')
        card1.costOre = 10
        db_committing_function(card1)
        round1 = Round(cardId=card1.id, playerId=player.id, round=game.round)
        db_committing_function(round1)
        
        #second wonder
        card2 = Card('test', 3, 1, 'brown')
        card2.costOre = 10
        db_committing_function(card2)
        round2 = Round(cardId=card2.id, playerId=player.id, round=game.round+1)
        db_committing_function(round2)
        
        #third wonder
        card3 = Card('test', 3, 1, 'brown')
        card3.costOre = 10
        db_committing_function(card3)
        round3 = Round(cardId=card3.id, playerId=player.id, round=game.round+2)
        db_committing_function(round3)
        
        #first wonder
        self.assertFalse(process_card(card1,player,False,True)['possible'])
        card = Card('testtest', 3, 1, 'brown')
        card.giveBrick = 2
        db_committing_function(card)
        ch = Cardhist(cardId=card.id, playerId=player.id)
        db_committing_function(ch)
        self.assertTrue(process_card(card1,player,False,True)['possible'])
        self.assertEqual(player.extra_brick, 1)
        
        #second wonder
        game.round = 2
        db_committing_function(game)
        self.assertFalse(process_card(card2,player,False,True)['possible'])
        card = Card('testtest2', 3, 1, 'brown')
        card.giveWood = 2
        db_committing_function(card)
        ch = Cardhist(cardId=card.id, playerId=player.id)
        db_committing_function(ch)
        stats = process_card(card2,player,False,True)
        print(stats)
        self.assertTrue(stats['possible'])
        self.assertEqual(player.extra_paper, 1)
        
        #third wonder
        game.round = 3
        db_committing_function(game)
        self.assertFalse(process_card(card3,player,False,True)['possible'])
        card = Card('testtest3', 3, 1, 'brown')
        card.giveStone = 3
        db_committing_function(card)
        ch = Cardhist(cardId=card.id, playerId=player.id)
        db_committing_function(ch)
        self.assertTrue(process_card(card3,player,False,True)['possible'])
        self.assertEqual(player.points, 7)

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
        combo = check_move_and_trade(card1, player1)
        self.assertFalse(combo['possible'])

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
        card2 = Card('test1', 3, 1, 'brown')
        card2.giveBrick = 1
        card3 = Card('test1', 3, 1, 'brown')
        card3.giveWood = 1
        db_committing_function(card1, card2, card3)

        ch1 = Cardhist(playerId=player1.id, cardId=card2.id)
        ch2 = Cardhist(playerId=player1.id, cardId=card3.id)
        db_committing_function(ch1, ch2)

        stats = check_move_and_trade(card1, player1)
        self.assertTrue(stats['left']['cost'] == 0)
        self.assertTrue(stats['right']['cost'] == 0)
        self.assertTrue(stats['possible'])

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
        card_hist = Card('test3', 3, 1, 'brown')
        card_hist.giveWood = 1
        db_committing_function(card1, card_left, card_hist)

        hist = Cardhist(playerId=player1.left_id, cardId=card_left.id, card_colour=card_left.colour)
        hist1 = Cardhist(playerId=player1.id, cardId=card_hist.id, card_colour=card_hist.colour)
        db_committing_function(hist, hist1)
        stats = check_move_and_trade(card1, player1)

        self.assertTrue(stats['possible'])
        self.assertTrue(
            stats['left']['Brick'] == 1 and
            stats['left']['cost'] == 2
        )
        
    def test_ai_makes_correct_move(self):
        user = User(email='test@test.com', name='test', password='tester')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        game = Game()
        game.age = 1
        db_committing_function(user, user1, user2, game)

        players = []
        player1 = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player1)
        player1.wood = 1
        player1.brick = 1
        player1.money = 0
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        card1 = Card('test', 3, 1, 'brown')
        card1.costBrick = 1
        card1.costWood = 1
        card1.giveMoney = 10000
        card2 = Card('test1', 3, 1, 'brown')
        card2.giveBrick = 1
        card3 = Card('test1', 3, 1, 'brown')
        card3.giveWood = 1
        db_committing_function(card1, card2, card3)
        
        round = Round(cardId=card1.id, playerId=player1.id)
        ch1 = Cardhist(playerId=player1.id, cardId=card2.id)
        ch2 = Cardhist(playerId=player1.id, cardId=card3.id)
        db_committing_function(ch1, ch2, round)
        
        print( [c.name for c in get_cards(player=player1, game=game)] )

        ai_move(player1, game)
        self.assertTrue(player1.money, 10000)
