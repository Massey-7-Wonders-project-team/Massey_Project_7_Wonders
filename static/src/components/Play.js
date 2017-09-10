import React from 'react';
import { RaisedButton, Dialog, FlatButton } from 'material-ui';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as actions from '../actions/game';
import GameScreen from './GameScreen';
import PlayerDisplay from './PlayerDisplay';

function mapStateToProps(state) {
    return {
        game: state.game.game,
        started: state.game.started,
        error: state.game.error,
        loading: state.game.loading,
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(actions, dispatch);
}


// we must export the class for testing. Then also default export the class
// at the end of the file which is used for the actual production render
export class Play extends React.Component {

    constructor() {
        super();
        this.state = {
            game: false,
            error: false,
            playerId: null,
            endGame: false,
        };
        this.createGame = this.createGame.bind(this);
        this.gameStatusCheck = this.gameStatusCheck.bind(this);
        this.handleClose = this.handleClose.bind(this);
        this.endGame = this.endGame.bind(this);
        this.endGameDialog = this.endGameDialog.bind(this);
    }

    componentDidMount() {
        // check if the user is already part of a game
        this.gameStatusCheck();
    }

    gameStatusCheck() {
        const token = localStorage.getItem('token');
        fetch('/api/game/check', {
            method: 'get',
            credentials: 'include',
            headers: {
                'Accept': 'application/json', // eslint-disable-line quote-props
                'Content-Type': 'application/json',
                Authorization: token,
            },
        })
        .then(response => response.json())
        .then((body) => {
            // do something
            console.log(body);
            if (body.player_id) {
                this.setState({
                    game: true,
                    error: false,
                    playerId: body.player_id,
                });
            } else {
                this.setState({
                    game: false,
                    error: false,
                });
            }
        })
        .catch((err) => {
            // catch error
            console.log(err);
            this.setState({
                game: false,
                error: true,
            });
        });
    }

    createGame() {
        // send request to create game
        const token = localStorage.getItem('token');
        fetch('/api/game/create', {
            method: 'get',
            credentials: 'include',
            headers: {
                'Accept': 'application/json', // eslint-disable-line quote-props
                'Content-Type': 'application/json',
                Authorization: token,
            },
        })
        .then(response => response.json())
        .then((body) => {
            // do something
            console.log(body);
            if (body.player_id) {
                this.setState({
                    game: true,
                    error: false,
                    playerId: body.player_id,
                });
            } else {
                this.setState({
                    game: false,
                    error: true,
                });
            }
        })
        .catch((err) => {
            // catch error
            console.log(err);
            this.setState({
                game: false,
                error: true,
            });
        });
    }

    endGame() {
        this.props.endGame(this.state.playerId);
        this.setState({
            endGame: false,
            playerId: null,
            game: false,
        });
    }

    handleClose() {
        this.setState({
            endGame: false,
        });
    }

    endGameDialog() {
        this.setState({
            endGame: true,
        });
    }

    render() {
        const { game, error, playerId,endGame } = this.state;
        const fullWidth = true;
        const primary = true;
        const endGameActions = [
            <FlatButton
                label="No"
                onClick={this.handleClose}
            />,
            <FlatButton
                label="Yes"
                onClick={this.endGame}
            />,
        ];
        return (
            <div className="Game col-md-12">
                <h1>Play</h1>

                <hr />
                {error &&
                    <p>There was an error</p>
                }
                {!game &&
                    <RaisedButton
                        label="Create/Join Game"
                        onClick={() => this.createGame()}
                    />
                }
                {game &&
                    <RaisedButton
                        label="End Game"
                        primary={primary}
                        style={{
                            float: 'right',
                            display: 'block',
                            margin: '0 0 20px 0',
                        }}
                        onClick={() => this.endGameDialog()}
                    />
                }
                {game &&
                    <div style={{ clear: 'both' }}>
                        <PlayerDisplay playerId={playerId} />
                        <GameScreen playerId={playerId} />
                    </div>
                }
                {endGame && game &&
                    <Dialog
                        title="Are you sure you want to end this game?"
                        actions={endGameActions}
                        open={this.state.endGame}
                        onRequestClose={this.handleClose}
                    >
                      Ending the game cannot be undone and ends it for all players.
                    </Dialog>
                }
            </div>
        );
    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(Play);
