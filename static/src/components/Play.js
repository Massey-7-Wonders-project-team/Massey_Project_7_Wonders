import React, { PropTypes } from 'react';
import { RaisedButton, Dialog, FlatButton, Paper, Checkbox } from 'material-ui';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { browserHistory } from 'react-router';
import * as actions from '../actions/game';
import GameScreen from './GameScreen';

function mapStateToProps(state) {
    return {
        game: state.game.game,
        started: state.game.started,
        error: state.game.error,
        loading: state.game.loading,
        clearInterval: state.game.clearInterval,
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(actions, dispatch);
}

const style = {
    marginTop: 50,
    padding: 50,
    marginLeft: 100,
    width: 'auto',
    textAlign: 'center',
    display: 'inline-block',
};

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
            playerCount: null,
            pollId: null,
            single: false,
        };
        this.createGame = this.createGame.bind(this);
        this.gameStatusCheck = this.gameStatusCheck.bind(this);
        this.handleClose = this.handleClose.bind(this);
        this.endGame = this.endGame.bind(this);
        this.endGameDialog = this.endGameDialog.bind(this);
        this.setPollId = this.setPollId.bind(this);
        this.updateCheck = this.updateCheck.bind(this);
    }

    componentDidMount() {
        // check if the user is already part of a game
        this.gameStatusCheck();
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.clearInterval === true) {
            this.endGame();
        }
    }

    gameStatusCheck() {
        const token = localStorage.getItem('token');
        fetch(`/api/game/check`, {
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
            if (body.player_id) {
                this.setState({
                    game: true,
                    error: false,
                    playerId: body.player_id,
                    playerCount: body.playerCount,
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
            console.error(err);
            this.setState({
                game: false,
                error: true,
            });
        });
    }

    createGame() {
        // send request to create game
        const token = localStorage.getItem('token');
        fetch(`/api/game/create?single_player=${this.state.single}`, {
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
            console.error(err);
            this.setState({
                game: false,
                error: true,
            });
        });
    }

    endGame() {
        this.props.endGame(this.state.playerId);
        clearInterval(this.state.pollId);
        this.setState({
            endGame: false,
            game: false,
        });
        browserHistory.push('/results');
    }

    setPollId(id) {
        this.setState({
            pollId: id,
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

    updateCheck() {
        this.setState((oldState) => {
          return {
            single: !oldState.single,
          };
        });
     }

    render() {
        const { game, error, playerId, endGame, playerCount } = this.state;
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
                {error &&
                    <p>There was an error</p>
                }
                {!game &&
                    <div>
                        <h1>Lets find a game...</h1>
                        <hr />
                        <div>
                            <Paper style={style}>
                                <h3>There are no active games for you</h3>
                                <p>Click below to create of join a new game</p>
                                <br />
                                <RaisedButton
                                    label="Create/Join Game"
                                    id="Play-CreateGame"
                                    onClick={() => this.createGame()}
                                />
                            </Paper>
                            <div
                                style={{
                                    padding: '30px',
                                    marginLeft: '80px',
                                    textAlign: 'left',
                                }}
                            >
                                <Checkbox
                                    id="single"
                                    onCheck={this.updateCheck}
                                    label="Check for single player mode"
                                />
                            </div>
                        </div>
                    </div>
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
                        <GameScreen playerId={playerId} setPollId={this.setPollId} />
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

Play.propTypes = {
    endGame: PropTypes.func.isRequired,
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(Play);
