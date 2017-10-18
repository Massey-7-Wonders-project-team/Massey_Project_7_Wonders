from flask import request, render_template, jsonify, url_for, redirect, g, session
from .controllers.state_printer import *
from .controllers.card_logic import *
from index import app
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
    if incoming.get("profile"):
        user = User(
            email=incoming["email"],
            name=incoming["profile"],
            password=incoming["password"]
        )
    else:
        user = User(
            email=incoming["email"],
            name="default user",
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
        profile=user.name,
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

    single_pl = false_true(request.args.get('single_player'))
    if single_pl:
        return single_player(user)

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
        player = Player(gameId=game.id, userId=user.id, name=user.name)
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


def single_player(user):
    no_players = request.args.get('number_of_players')
    if not no_players:
        no_players = 7
    game = Game()
    game.single_player = True
    db_committing_function(game)

    player_human = Player(gameId=game.id, userId=user.id, name=user.name)

    users_ai = User.query.filter(User.id.in_(range(1, 7))).all()
    players_ai = []
    for i in range(1, no_players):
        user = users_ai.pop()
        players_ai.append(Player(gameId=game.id, userId=user.id, name=user.name, ai=True))
        players_ai[i - 1].ready = True

    db_committing_function(player_human, players_ai)
    return jsonify(
        player_id=player_human.id,
        playerCount=no_players
    )


@app.route("/api/game/status", methods=["GET"])
@requires_auth
def game_status():
    """ Send the status of a game
     Inputs - player_id
     Output
        Game not started - status comment, playerCount
        Game started - status comment, game (player, cards), playerCount """
    # firstly check game has started
    try:
        player = get_player(request.args.get('player_id'))
        game = get_game(player=player)
        players = get_players(player=player)
        player_count = len(players)

        if not game.started:
            return jsonify(
                status="Waiting",
                playerCount=player_count
            )
        elif game.complete:
            return jsonify(
                status="Completed",
                game=print_json(player, players=players, game=game),
                players=player_count
            )
        else:
            return jsonify(
                status="Started",
                game=print_json(player, players=players, game=game),
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
        If player was already ready - status comment
        Game not started - status comment
        Game started - status comment, game (player, cards)"""
    player = get_player(request.args.get('player_id'))

    # Only continues if player was not already set as ready
    if player.ready is False:
        player.ready = True
    else:
        print(player.id, "was already set as ready")
        return game_status()

    db_committing_function(player)

    ############################
    # Checks if game can begin #
    ############################
    players = get_players(player=player)
    player_count = len(players)

    if player_count > 2:
        if player_count < 7:
            for p in players:
                if p.ready is False:
                    print("Player "+ str(p.id) +" not ready")
                    return jsonify(status="Waiting")

        # Game can begin
        game = get_game(player=player)
        game.started = True

        # Sets up neighbours and first round
        set_player_neighbours(players)
        if not request.args.get('test'):
            deal_wonders(players)
            age_calcs_and_dealing(players, game)

        # DB update and begin game
        db_committing_function(game)
        return jsonify(
            status="Starting",
            game=print_json(player, players=players)
        )

    else:
        print("not enough players")
        return jsonify(status="Waiting")

@app.route("/api/game/play_card", methods=["GET"])
@requires_auth
def play_card():
    """Endpoint for all card playing actions
    Inputs - player_id, card_id, discarded (bool), and for_wonder(bool)
    Outputs - status comment"""
    player = get_player(request.args.get('player_id'))
    card = get_card(request.args.get('card_id'))
    discarded = false_true(request.args.get('discarded'))
    for_wonder = false_true(request.args.get('for_wonder'))
    from_discard_pile = false_true(request.args.get('from_discard_pile'))
    trade = false_true(request.args.get('trade'))

    if process_card(card, player, discarded, for_wonder, from_discard_pile=from_discard_pile, tr=trade):
        return jsonify(status="Card played")
    else:
        return jsonify(
            status="Invalid move",
            game=print_json(player)
        )

@app.route("/api/game/end", methods=["GET"])
@requires_auth
def end_game():
    """Endpoint for ending a game mid game
    Inputs - player_id
    Outputs - status comment"""
    player = get_player(request.args.get('player_id'))
    game = get_game(player=player)
    game.complete = True
    db.session.add(game)

    try:
        print('Ending game')
        db.session.commit()
        return jsonify(message="Success")
    
    except Exception as e:
        print(e)
        return jsonify(message="There was an error"), 500

@app.route("/api/game/result", methods=["GET"])
@requires_auth
def game_result():
    """Endpoint for ending a game mid game
    Inputs - player_id
    Outputs - status comment"""
    player = Player.query.join(User).filter_by(email=g.current_user["email"]).join(Game).order_by(Game.id.desc()).filter_by(complete=True).first()
    game = get_game(player=player)
    players = get_players(player=player)
    player_count = len(players)

    try:
        return jsonify(
            status="Completed",
            game=print_json(player, players=players, game=game),
            players=player_count
        )

    except Exception as e:
        print(e)
        return jsonify(message="There was an error"), 500
