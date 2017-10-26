from testing_config import BaseTestConfig
from flask_testing import TestCase
import json
from application.utils import auth
from application.app import *

class TestAPI(BaseTestConfig):
    some_user = {
        "email": "one@gmail.com",
        "password": "something1"
    }

    def test_get_spa_from_index(self):
        result = self.app.get("/")
        self.assertIn('<html>', result.data.decode("utf-8"))

    def test_create_new_user(self):
        self.assertIsNone(User.query.filter_by(
                email=self.some_user["email"]
        ).first())

        res = self.app.post(
                "/api/create_user",
                data=json.dumps(self.some_user),
                content_type='application/json'
        )
        self.assertEqual(res.status_code, 200)
        self.assertTrue(json.loads(res.data.decode("utf-8"))["token"])
        self.assertEqual(User.query.filter_by(email=self.some_user["email"]).first().email, self.some_user["email"])

        res2 = self.app.post(
                "/api/create_user",
                data=json.dumps(self.some_user),
                content_type='application/json'
        )

        self.assertEqual(res2.status_code, 409)

    def test_get_token_and_verify_token(self):
        res = self.app.post(
                "/api/get_token",
                data=json.dumps(self.default_user),
                content_type='application/json'
        )

        token = json.loads(res.data.decode("utf-8"))["token"]
        self.assertTrue(auth.verify_token(token))
        self.assertEqual(res.status_code, 200)

        res2 = self.app.post(
                "/api/is_token_valid",
                data=json.dumps({"token": token}),
                content_type='application/json'
        )

        self.assertTrue(json.loads(res2.data.decode("utf-8")), ["token_is_valid"])

        res3 = self.app.post(
                "/api/is_token_valid",
                data=json.dumps({"token": token + "something-else"}),
                content_type='application/json'
        )

        self.assertEqual(res3.status_code, 403)

        res4 = self.app.post(
                "/api/get_token",
                data=json.dumps(self.some_user),
                content_type='application/json'
        )

        self.assertEqual(res4.status_code, 403)

    def test_protected_route(self):
        headers = {
            'Authorization': self.token,
        }

        bad_headers = {
            'Authorization': self.token + "bad",
        }

        response = self.app.get('/api/user', headers=headers)
        self.assertEqual(response.status_code, 200)
        response2 = self.app.get('/api/user')
        self.assertEqual(response2.status_code, 401)
        response3 = self.app.get('/api/user', headers=bad_headers)
        self.assertEqual(response3.status_code, 401)


class TestAPIAlchemy(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_check_game(self):
        user = User(email='test@test.com', name='test', password='tester')
        game = Game()
        db_committing_function(user, game)
        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/check",
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res.status_code, 200)
        self.assertTrue(json.loads(res.data.decode("utf-8")), ['Need to join game'])

        player = Player(gameId=game.id, userId=user.id, name=user.name)
        db_committing_function(player)
        res2 = self.client.get(
            "/api/game/check",
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res2.status_code, 200)
        assert b'player_id' in res2.data

    def test_create_game(self):
        user = User(email='test@test.com', name='test', password='tester')
        db_committing_function(user)
        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/create?single_player=false",
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res.status_code, 200)
        assert b'"player_id": 1' in res.data
        assert b'"playerCount": 1' in res.data

    def test_create_game_single_player(self):
        user = User(email='test@test.com', name='test', password='tester')
        ai = []
        for i in range(6):
            name = 'Computer Player ' + str(i + 1)
            ai.append(User(
                email=i,
                name=name,
                password=name + str(i)
            ))
        db_committing_function(user, ai)

        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/create?single_player=true",
            headers={
                'Authorization': token,
            }
        )

        player = get_player(json.loads(res.data.decode("utf-8")).get('player_id'))
        game = get_game(player=player)

        self.assertEqual(res.status_code, 200)
        assert b'"player_id": 1' in res.data
        assert b'"playerCount": 3' in res.data
        self.assertTrue(game.single_player)

    def test_game_status_not_started(self):
        user = User(email='test@test.com', name='test', password='tester')
        game = Game()
        db_committing_function(user, game)
        player = Player(gameId=game.id, userId=user.id, name=user.name)
        db_committing_function(player)

        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/status?player_id="+str(player.id),
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res.status_code, 200)
        assert b'Waiting' in res.data
        assert b'"playerCount": 1' in res.data

    def test_game_status_started(self):
        user = User(email='test@test.com', name='test', password='tester')
        game = Game(started=True)
        db_committing_function(user, game)
        player = Player(gameId=game.id, userId=user.id, name=user.name)
        db_committing_function(player)

        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/status?player_id="+str(player.id),
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res.status_code, 200)
        assert b'Started' in res.data
        assert b'"players": 1' in res.data
        assert b'game' in res.data

    def test_begin_game_1_player(self):
        user = User(email='test@test.com', name='test', password='tester')
        game = Game()
        db_committing_function(user, game)
        player = Player(gameId=game.id, userId=user.id, name=user.name)
        db_committing_function(player)

        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/start?player_id=" + str(player.id),
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res.status_code, 200)
        assert b'Waiting' in res.data

    def test_begin_game_2_players(self):
        user = User(email='test@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        game = Game()
        db_committing_function(user, user2, game)
        player = Player(gameId=game.id, userId=user.id, name=user.name)
        player2 = Player(gameId=game.id, userId=user2.id, name=user2.name)
        db_committing_function(player, player2)

        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/start?player_id=" + str(player.id),
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res.status_code, 200)
        assert b'Waiting' in res.data

    def test_begin_game_3_players_not_ready(self):
        user = User(email='test@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        user3 = User(email='test3@test.com', name='test', password='tester')
        game = Game()
        db_committing_function(user, user2, user3, game)
        player = Player(gameId=game.id, userId=user.id, name=user.name)
        player2 = Player(gameId=game.id, userId=user2.id, name=user2.name)
        player3 = Player(gameId=game.id, userId=user3.id, name=user3.name)
        db_committing_function(player, player2, player3)

        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/start?player_id=" + str(player.id),
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res.status_code, 200)
        assert b'Waiting' in res.data

    def test_begin_game_3_players_ready(self):
        user = User(email='test@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        user3 = User(email='test3@test.com', name='test', password='tester')
        game = Game()
        db_committing_function(user, user2, user3, game)
        player = Player(gameId=game.id, userId=user.id, name=user.name)
        player2 = Player(gameId=game.id, userId=user2.id, name=user2.name, ready=True)
        player3 = Player(gameId=game.id, userId=user3.id, name=user3.name, ready=True)
        db_committing_function(player, player2, player3)

        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/start?player_id=" + str(player.id)+"&test=True",
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res.status_code, 200)
        assert b'Starting' in res.data
        assert b'game' in res.data
        self.assertTrue(game.started)
        self.assertTrue(player.left_id and player.right_id)
        self.assertTrue(player2.left_id and player2.right_id)
        self.assertTrue(player3.left_id and player3.right_id)

    def test_begin_game_already_ready(self):
        user = User(email='test@test.com', name='test', password='tester')
        game = Game()
        db_committing_function(user, game)
        player = Player(gameId=game.id, userId=user.id, name=user.name, ready=True)
        db_committing_function(player)

        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/start?player_id=" + str(player.id),
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res.status_code, 200)
        assert b'Waiting' in res.data
        assert b'"playerCount": 1' in res.data

    def test_end_game(self):
        user = User(email='test@test.com', name='test', password='tester')
        game = Game(started=True)
        db_committing_function(user, game)
        player = Player(gameId=game.id, userId=user.id, name=user.name)
        db_committing_function(player)

        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/end?player_id=" + str(player.id),
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res.status_code, 200)
        assert b'Success' in res.data
        self.assertTrue(game.complete)

    def test_play_card_discarded(self):
        user = User(email='test@test.com', name='test', password='tester')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        game = Game(age=1)
        card = Card('test', 3, 1, 'brown')
        db_committing_function(user, user1, user2, game, card)

        players = []
        player = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player)
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        round = Round(playerId=player.id, cardId=card.id)
        db_committing_function(round)

        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/play_card?player_id=" + str(player.id) +
            "&card_id=" + str(card.id) + "&discarded=true&for_wonder=false",
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res.status_code, 200)
        assert b'"possible": true' in res.data
        self.assertFalse(get_cards(player=player, history=True))
        self.assertTrue(player.money == 6)

    def test_play_card_played(self):
        user = User(email='test@test.com', name='test', password='tester')
        user1 = User(email='test1@test.com', name='test', password='tester')
        user2 = User(email='test2@test.com', name='test', password='tester')
        game = Game(started=True, age=1, round=1)
        card = Card("Clay Pool", 3, 1, "brown")
        db_committing_function(user, user1, user2, game, card)

        players = []
        player = Player(gameId=game.id, userId=user.id, name=user.name)
        players.append(player)
        players.append(Player(gameId=game.id, userId=user1.id, name=user1.name))
        players.append(Player(gameId=game.id, userId=user2.id, name=user2.name))
        db_committing_function(players)
        set_player_neighbours(players)

        round = Round(playerId=player.id, cardId=card.id)
        db_committing_function(round)

        token = auth.generate_token(user)
        res = self.client.get(
            "/api/game/play_card?player_id=" + str(player.id) +
            "&card_id=" + str(card.id) + "&discarded=false&for_wonder=false",
            headers={
                'Authorization': token,
            }
        )

        self.assertEqual(res.status_code, 200)
        assert b'"possible": true' in res.data
        self.assertTrue(get_cards(player=player, history=True))

    # TODO Test wonder card track
