from flask import request, render_template, jsonify, url_for, redirect, g, flash, session
from .models.user import User
from .models.game import Game
from .models.card import Card
from .models.player import Player
from .models.round import Round
from .controllers.state import *
from .controllers.logic import *
from index import app, db
from sqlalchemy.exc import IntegrityError
from .utils.auth import generate_token, requires_auth, verify_token


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('index.html')


@app.route("/api/user", methods=["GET"])
@requires_auth
def get_user():
    return jsonify(result=g.current_user)


@app.route("/api/create_user", methods=["POST"])
def create_user():
    incoming = request.get_json()
    user = User(
        email=incoming["email"],
        password=incoming["password"]
    )
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        return jsonify(message="User with that email already exists"), 409

    new_user = User.query.filter_by(email=incoming["email"]).first()

    return jsonify(
        id=user.id,
        token=generate_token(new_user)
    )


@app.route("/api/get_token", methods=["POST"])
def get_token():
    incoming = request.get_json()
    username = incoming["email"]
    password = incoming["password"]
    user = User.get_user_with_email_and_password(username, password)
    if user:
        return jsonify(token=generate_token(user))

    return jsonify(error=True), 403


@app.route("/api/is_token_valid", methods=["POST"])
def is_token_valid():
    incoming = request.get_json()
    is_valid = verify_token(incoming["token"])

    if is_valid:
        return jsonify(token_is_valid=True)
    else:
        return jsonify(token_is_valid=False), 403

@app.route("/api/game/check", methods=["GET"])
@requires_auth
def check_game():
    """ Check if a user has already joined a game """
    player = Player.query.join(User).filter_by(email=g.current_user["email"]).join(Game).filter_by(complete=False).first()

    if player is None:
        return jsonify(
            status="Need to join game"
        )

    return jsonify(
        player_id=player.id
    )

@app.route("/api/game/create", methods=["GET"])
@requires_auth
def create_game():
    """ Check if game exists and add user to it else create new game """
    user = User.query.filter_by(email=g.current_user["email"]).first()
    print("user: ", user.id)
    game = Game.query.filter_by(started=False).first()

    # Creates game if there is no active one waiting to begin
    if game is None:
        game = Game()
        db.session.add(game)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify(message="There was an error"), 501

    # Creates and commits new player, binds to the current game and user
    player = Player(gameId=game.id, userId=user.id)
    db.session.add(player)

    player_count = len(Player.query.filter_by(gameId=game.id).all())

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify(message="There was an error"), 501

    return jsonify(
        player_id=player.id,
        playerCount=player_count
    )

@app.route("/api/game/status", methods=["GET"])
@requires_auth
def game_status():
    """ Send the status of a game """
    # firstly check game has started
    try:
        player_id = request.args.get('player_id')
        player = Player.query.filter_by(id=player_id).first()
        game = Game.query.filter_by(id=player.gameId).first()
        players = Player.query.filter_by(gameId=game.id).all()
        player_count = len(players)
        if not game.started:
            return jsonify(
                status="Waiting",
                playerCount=player_count
            )
        else:
            cards = (Round.query
                     .filter_by(playerId=player.id)
                     .filter_by(age=game.age)
                     .filter_by(round=game.round)
                     .join(Card)).all()
            # Game has started return full game state
            return jsonify(
                status="Started",
                game=print_json(player, cards),
                players=player_count
            )

    except Exception as e:
        print(e)
        return jsonify(message="There was an error"), 501

@app.route("/api/game/start", methods=["GET"])
@requires_auth
def begin_game():
    player_id = request.args.get('player_id')
    player = Player.query.filter_by(id=player_id).first()
    player.ready = True
    db.session.add(player)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify(message="There was an error"), 501

    # print("Player: " + player.id + " Ready: " + player.ready)
    players = Player.query.filter_by(gameId=player.gameId).all()
    print(players);
    # IF EVERY PLAYER IS READY, AND THERE ARE AT LEAST 3, THEN THE GAME STARTS, OTHERWISE THE GAME WAITS:
    if len(players) > 2:
        for p in players:
            if p.ready == False:
                print("Players not ready")
                return jsonify(status="Waiting")
        game = Game.query.filter_by(id=player.gameId).first()
        game.started = True
        db.session.add(game)
        deal_hands(1, players)

        cards = Round.query.filter_by(playerId=player.id).join(Card).all()
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify(message="There was an error"), 501
        return jsonify(
            status="Starting",
            game=print_json(player, cards)
        )

    else:
        print ("not enough players")
        return jsonify(status="Waiting")

@app.route("/api/game/play_card", methods=["GET"])
@requires_auth
def play_card():
    player_id = request.args.get('player_id')
    card_id = request.args.get('card_id')
    discarded = request.args.get('discarded')
    player = Player.query.filter(id=player_id).first()
    card = Card.query.filter(id=card_id).first()

    if process_card(card, player, discarded, False):
        return jsonify(status="Card played")
    else:
        game = Game.query.filter_by(id=player.gameId).first()
        cards = Round.query.filter_by(playerId=player.id, age=game.age, round=game.round).all()
        return jsonify(
            status="Invalid move",
            game=print_json(player, cards)
        )
