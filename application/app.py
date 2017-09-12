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
        return jsonify(message="There was an error"), 500

    # Creates and commits new player, binds to the current game and user
    players = Player.query.filter_by(gameId=game.id, userId=user.id).all()

    if not players:
        player = Player(gameId=game.id, userId=user.id)
        db.session.add(player)
    else:
        print("Player already exists in this game")
        player_count = len(Player.query.filter_by(gameId=game.id).all())
        return jsonify(
            player_id=players[0].id,
            playerCount=player_count
        )

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify(message="There was an error"), 500

    player_count = len(Player.query.filter_by(gameId=game.id).all())
    return jsonify(
        player_id=player.id,
        playerCount=player_count
    )

@app.route("/api/game/status", methods=["GET"])
@requires_auth
def game_status():
    """ Send the status of a game
     Inputs - player_id, (later) is_owned_by_player (bool)
     Output
        Game not started - status comment, playerCount
        Game started - status comment, game (player, cards), playerCount """
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
            card_ids = [card[0] for card in db.session.query(Round.cardId).filter_by(playerId=player.id, age=game.age, round=game.round).all()]
            cards = Card.query.filter(Card.id.in_(card_ids)).all()

            # the following checks to see if the player has played a card in the next round
            # which means it is waiting for other players to play this round
            if Round.query.filter_by(playerId=player.id, round=game.round+1, age=game.age).first():
                return jsonify(
                    status="Card Played",
                    game=print_json(player, players, cards),
                    players=player_count,
                    played_card=(Cardhist.query.filter(Cardhist.cardId.in_(card_ids)).filter_by(playerId=player.id).first()).serialise()
                )
            return jsonify(
                status="Started",
                game=print_json(player, players, cards),
                players=player_count
            )

    except Exception as e:
        print(e)
        return jsonify(message="There was an error"), 500

@app.route("/api/game/start", methods=["GET"])
@requires_auth
def begin_game():
    """This endpoint is for once a player is ready to start. Will begin a game if all players (3+)
    are ready or there are 7 players
    Inputs - player_id
    Outputs -
        Game not started - status comment
        Game started - status comment, game (player, cards)"""
    player_id = request.args.get('player_id')
    player = Player.query.filter_by(id=player_id).first()

    # Only continues if player was not already set as ready
    if player.ready is False:
        player.ready = True
    else:
        print(player_id, "was already set as ready")
        return game_status()

    try:
        db.session.add(player)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify(message="There was an error"), 500

    ############################
    # Checks if game can begin #
    ############################
    players = Player.query.filter_by(gameId=player.gameId).all()
    player_count = len(players)

    if player_count > 2:
        if player_count < 7:
            for p in players:

                counter = 0
                for i in range(len(players)):
                    if p.id is players[i].id:
                        counter += 1
                if counter > 1:
                    continue

                if p.ready == False:
                    print("Players not ready")
                    return jsonify(status="Waiting")
        # Game can begin
        game = Game.query.filter_by(id=player.gameId).first()
        game.started = True

        # Sets up neighbours and first round
        set_neighbours(players)
        deal_wonders(players)
        age_calcs_and_dealing(players, game)

        military_calcs(players, 1)

        # DB update and begin game
        cards = Round.query.filter_by(playerId=player.id).join(Card).all()
        try:
            db.session.add(game)
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify(message="There was an error"), 500
        return jsonify(
            status="Starting",
            game=print_json(player, players, cards)
        )

    else:
        print ("not enough players")
        return jsonify(status="Waiting")

@app.route("/api/game/play_card", methods=["GET"])
@requires_auth
def play_card():
    """Endpoint for all card playing actions
    Inputs - player_id, card_id, discarded (bool), and (later on) for_wonder(bool)
    Outputs - status comment"""
    player_id = request.args.get('player_id')
    card_id = request.args.get('card_id')
    discarded = false_true(request.args.get('discarded'))
    for_wonder = false_true(request.args.get('for_wonder'))

    player = Player.query.filter_by(id=player_id).first()
    card = Card.query.filter_by(id=card_id).first()

    if process_card(card, player, discarded, for_wonder):
        return jsonify(status="Card played")
    else:
        game = Game.query.filter_by(id=player.gameId).first()
        cards = Round.query.filter_by(playerId=player.id, age=game.age, round=game.round).all()
        players = Player.query.filter_by(gameId=player.gameId).all()
        return jsonify(
            status="Invalid move",
            game=print_json(player, players, cards)
        )

@app.route("/api/game/end", methods=["GET"])
@requires_auth
def end_game():
    """Endpoint for ending a game mid game
    Inputs - player_id
    Outputs - status comment"""
    player_id = request.args.get('player_id')
    player = Player.query.filter_by(id=player_id).first()
    game = Game.query.filter_by(id=player.gameId).first()
    game.complete = True
    db.session.add(game)

    try:
        print('Ending game')
        db.session.commit()
        return jsonify(message="Success")

    except Exception as e:
        print(e)
        return jsonify(message="There was an error"), 500
