import React, { PropTypes } from 'react';
import { RaisedButton, Dialog, FlatButton, Paper,
  DropDownMenu, MenuItem, Checkbox } from 'material-ui';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { browserHistory } from 'react-router';
import * as actions from '../actions/game';
import GameScreen from './GameScreen';
import MilitaryUpdate from './MilitaryUpdate';

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
            militaryDialog: false,
            militaryOnce: false,
            value: 6,
            aiPlayers: 0,
        };
        this.createGame = this.createGame.bind(this);
        this.gameStatusCheck = this.gameStatusCheck.bind(this);
        this.handleClose = this.handleClose.bind(this);
        this.endGame = this.endGame.bind(this);
        this.endGameDialog = this.endGameDialog.bind(this);
        this.setPollId = this.setPollId.bind(this);
        this.updateCheck = this.updateCheck.bind(this);
        this.hideArmyDialog = this.hideArmyDialog.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    componentDidMount() {
        // check if the user is already part of a game
        this.gameStatusCheck();
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.clearInterval === true) {
            this.setState({
                militaryDialog: true,
                militaryOnce: true,
            })
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
                    militaryOnce: false,
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
        fetch(`/api/game/create?single_player=${this.state.single}&ai_players=${this.state.value}`, {
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

     hideArmyDialog() {
         this.setState({
             militaryDialog: false,
         });
         this.endGame();
     }

     handleChange = (event, index, value) => this.setState({value});

    render() {
        const { game, error, playerId, endGame, playerCount } = this.state;
        const primary = true;
        const endGameActions = [
            <FlatButton
                label="No"
                onTouchTap={this.handleClose}
            />,
            <FlatButton
                label="Yes"
                onTouchTap={this.endGame}
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
                        <div>
                            <Paper style={style}>
                                <h3>There are no active games for you</h3>
                                <p>Click below to create of join a new game</p>
                                <br />
                                <RaisedButton
                                    label="Create/Join Game"
                                    id="Play-CreateGame"
                                    onTouchTap={() => this.createGame()}
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
                                    label=" Single player mode against"
                                    style={{ clear: 'left', float: 'left', width: 240 }}
                                />
                                <DropDownMenu
                                    id="PlayerSelection"
                                    value={this.state.value}
                                    onChange={this.handleChange}
                                    style={{ marginTop: -15, marginLeft: -35, paddingLeft: 0, width: 150, float: 'left', lineHeight: 30 }}
                                    menuStyle={{ marginLeft: 0, padding: 0 }}
                                >
                                    <MenuItem value={6} primaryText={<b>6 players</b>} />
                                    <MenuItem value={5} primaryText={<b>5 players</b>} />
                                    <MenuItem value={4} primaryText={<b>4 players</b>} />
                                    <MenuItem value={3} primaryText={<b>3 players</b>} />
                                    <MenuItem value={2} primaryText={<b>2 players</b>} />
                                </DropDownMenu>
                            </div>
                        </div>
                    </div>
                }
                {game && this.props.game &&
                <div>
                    <div style={{ float: 'left', marginRight: 0, paddingTop: 0, paddingLeft: 50, width: '20%' }}>
                        <h3 style={{ marginTop: 0}}>
                            <b>Age: {this.props.game.game.age} -
                            Round: {this.props.game.game.round}
                            </b>
                        </h3>
                    </div>
                    <div style={{ float: 'left', marginRight: 0, paddingTop: 0, width: '60%' }}>
                        <center><h3 style={{ marginTop: 0 }}> Cards in Hand </h3></center>
                    </div>
                    <RaisedButton
                        label="End Game"
                        primary={primary}
                        style={{
                            float: 'right',
                            display: 'block',
                            margin: '0 0 20px 0',
                        }}
                        onTouchTap={() => this.endGameDialog()}
                    />
                </div>
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
                {this.state.militaryDialog && this.state.militaryOnce &&
                  <Dialog
                      id="armyDialog"
                      title={`Military Updates at end of Age 3`}
                      actions={
                          <FlatButton
                              label="Close"
                              primary={true}
                              onClick={this.hideArmyDialog}
                          />
                      }
                      open={this.state.militaryDialog}
                      onRequestClose={this.hideArmyDialog}
                      contentStyle={{ width: '100%' }}
                  >
                      <MilitaryUpdate data={this.props.game} />
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
