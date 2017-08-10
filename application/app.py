from flask import request, render_template, jsonify, url_for, redirect, g, flash, session
from .models.user import User
from .models.game import Game
from .models.card import Card
from .models.player import Player
from .models.round import Round
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
    player = (Player.query.join(User).filter_by(email=g.current_user["email"])
            .join(Game).filter_by(started=False)).first()

    print(player)
    return jsonify(
        game_id=player.gameId
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
    print("game: ", game.id)

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
        game_id=game.id,
        players=player_count
    )

@app.route("/api/game/status", methods=["GET"])
@requires_auth
def game_status():
    """ Send the status of a game """

    # firstly check game has started
    try:
        game_id = request.args.get('game_id')
        game = Game.query.filter_by(gameId = game_id)

        if (game.started == False):
            return jsonify(status="Waiting")
        else:
            # Game has started return full game state
            return jsonify(
                status="Started"
            )

    except Exception as e:
        print(e)
        return jsonify(message="There was an error"), 501

@app.route("/api/game/start", methods=["GET"])
@requires_auth
def begin_game():
    table = (Player.query.join(User).join(Game).
             filter_by(email=g.current_user["email"]).
             filter_by(started=False)).first()
    player = Player.query.filter(gameId=table.gameId, userId=table.userId)
    player.ready = True
    db.session.add(player)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify(message="There was an error"), 501

    print("User: " + player.userId + " Game: " + player.gameId + " Ready: " + player.ready)
    players = Player.query.filter_by(gameId=table.gameId).all()

    # IF EVERY PLAYER IS READY, AND THERE ARE AT LEAST 3, THEN THE GAME STARTS, OTHERWISE THE GAME WAITS:
    if len(players) > 2:
        for p in players:
            if p.ready == False:
                flash("Please wait for other players")
                return jsonify(
                    game_id=table.gameId,
                )
        flash("Game starting")
        game = Game.query.filter_by(id=table.gameId).first()
        game.started = True
        db.add(game)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify(message="There was an error"), 501
        return jsonify(
            game_id=table.gameId,
        ) #dealHands(table.gameId, 1) TODO

    else:
        flash("Please wait for other players")
        return jsonify(
            game_id=table.gameId,
        )
