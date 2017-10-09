import React, { PropTypes, Component } from 'react';
import { RaisedButton, CardActions, FlatButton, Card,
    CardText, CardMedia, CardTitle, CircularProgress, Dialog } from 'material-ui';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as actions from '../actions/game';
import { poll } from '../utils/misc';
import PlayerDisplay from './PlayerDisplay';
import EndScreen from './EndScreen';

function mapStateToProps(state) {
    return {
        game: state.game.game,
        started: state.game.started,
        error: state.game.error,
        loading: state.game.loading,
        playerCount: state.game.playerCount,
        cardPlayed: state.game.cardPlayed,
        cardValid: state.game.cardValid,
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(actions, dispatch);
}

export class GameScreen extends Component {

    constructor() {
        super();
        this.state = {
            polling: false,
            showPlayCardError: false,
            pollId: null,
            playerCount: null,
            ready: false,
            endOfRound: false,
            ageDialog: false,
            ageDialogDisplayOnce: false,
            showScoreBoard: false,
            shownForRound: false,
            endGameScoreboard: false,
            showInvalidMoveError: false,
        };
        this.startGame = this.startGame.bind(this);
        this.pollGameStatus = this.pollGameStatus.bind(this);
        this.hidePlayCardError = this.hidePlayCardError.bind(this);
        this.playersLogged = this.playersLogged.bind(this);
        this.hideScoreboard = this.hideScoreboard.bind(this);
        this.hideInvalidMoveError = this.hideInvalidMoveError.bind(this);
        this.hideAgeDialog = this.hideAgeDialog.bind(this);
    }

    componentDidMount() {
        this.props.checkGameStatus(this.props.playerId);
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.cardValid === false) {
            console.log('INVALID')
            this.setState({
                showInvalidMoveError: true,
            });
        }

        if (nextProps.game) {
            if (!this.state.shownForRound &&
                nextProps.game.game.round === 1 && nextProps.game.game.age !== 1) {
                this.setState({
                    showScoreBoard: true,
                    shownForRound: true,
                });
            }
            if (nextProps.game.game.round === 2) {
                this.setState({
                    shownForRound: false,
                    ageDialogDisplayOnce: false,
                    ageDialog: false,
                });
            }
        }

        if (nextProps.started && !this.state.polling) {
            this.setState({
                polling: true,
            });
            this.pollGameStatus();
        }
        if (nextProps.game.game.round === 1) {
            this.setState({
                ageDialog: true,
            });
        }
    }

    pollGameStatus() {
        const pollId = poll(() => this.props.checkGameStatus(this.props.playerId), 1000);
        this.props.setPollId(pollId);
    }

    startGame() {
        if (!this.state.ready) {
            this.setState({
                ready: true,
            })
        }
        this.props.startGame(this.props.playerId);
    }

    // playCard(playerId, cardId, discarded, wonder, trade)

    playCard(cardId) {
        if (!this.props.cardPlayed) {
            this.props.playCard(this.props.playerId, cardId, false, false, true);
        } else {
            this.setState({
                showPlayCardError: true,
            });
        }
    }

    wonderCard(cardId) {
        if (!this.props.cardPlayed) {
            this.props.playCard(this.props.playerId, cardId, false, true, true);
        } else {
            this.setState({
                showPlayCardError: true,
            });
        }
    }

    discard(cardId) {
        if (!this.props.cardPlayed) {
            this.props.playCard(this.props.playerId, cardId, true, false, false);
        } else {
            this.setState({
                showPlayCardError: true,
            });
        }
    }

    hidePlayCardError() {
        this.setState({
            showPlayCardError: false,
        });
    }

    hideScoreboard() {
        this.setState({
            showScoreBoard: false,
        });
    }

    hideInvalidMoveError() {
        this.props.clearInvalidCardError();
        this.setState({
            showInvalidMoveError: false,
        });
    }

    hideAgeDialog() {
        this.setState({
            ageDialog: false,
            ageDialogDisplayOnce: true,
        });
    }

    playersLogged() {
        const token = localStorage.getItem('token');
        fetch(`/api/game/status?player_id=${this.props.playerId}`, {
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
          if (this.state.playerCount < body.playerCount) {
              this.setState({
                  playerCount: body.playerCount,
              });
          }
      });
    }

    render() {
        const { error, game, started, loading } = this.props;
        const { showPlayCardError, showScoreBoard, showInvalidMoveError } = this.state;
        const showPlayCardActions = [
            <FlatButton
                label="Ok"
                onClick={this.hidePlayCardError}
            />,
        ];
        const showInvalidMoveActions = [
            <FlatButton
                label="Ok"
                onClick={this.hideInvalidMoveError}
            />,
        ];
        if (!started) {
            this.playersLogged();
        }

        if (started && game.game.age) {
          document.title = `Age: ${game.game.age} Round: ${game.game.round}`;
        }


        return (
            <div>
                {game && !error && started &&
                    <div>
                        <div>
                            {game.playedCards &&
                                game.playedCards.map((pcard) => {
                                    const imageName = (pcard.card.name).replace(/\s+/g, '').toLowerCase();
                                    return (
                                        <Card key={pcard.id} style={{ width: 130, display: 'inline-block' }}>
                                            <CardTitle title={pcard.card.name} />
                                            <CardMedia>
                                                <img
                                                    alt={`${pcard.card.name}`}
                                                    src={`dist/images/cards/${imageName}.png`}
                                                />
                                            </CardMedia>
                                        </Card>
                                    );
                                })
                            }
                            {this.state.ageDialog && !this.state.ageDialogDisplayOnce &&
                                <Dialog
                                    title={`Age ${game.game.age} is about to begin...`}
                                    actions={
                                        <FlatButton
                                            label="Begin"
                                            primary={true}
                                            onClick={this.hideAgeDialog}
                                        />
                                    }
                                    open={this.state.ageDialog}
                                    onRequestClose={this.hideAgeDialog}
                                    contentStyle={{ width: '40%' }}
                                >
                                  <center><div>

                                      <img height="75%" src={`dist/images/icons/age${game.game.age}cards.png`} />
                                  </div></center>
                                </Dialog>
                            }
                            <div>
                                {showScoreBoard &&
                                    <EndScreen
                                        hideScoreboard={this.hideScoreboard}
                                        endGameScoreboard={this.state.endGameScoreboard}
                                    />
                                }
                            </div>
                            <center>
                            {game.cards && game.cards[0].name &&
                                game.cards.map((card, index) => {
                                    const imageName = (card.name).replace(/\s+/g, '').toLowerCase();
                                    return (
                                        <Card className="Card" data-card-number={index} key={card.id} style={{ marginRight: 5, width: 130, display: 'inline-block', paddingBottom: 0 }}>
                                            <CardTitle
                                                title={card.name}
                                                titleStyle={{ fontSize: 18 }}
                                                style={{ padding: 3, height: 75 }}
                                            />
                                            <CardMedia>
                                                <img
                                                    alt={`${card.name} image`}
                                                    src={`dist/images/cards/${imageName}.png`}
                                                />
                                            </CardMedia>
                                            <CardActions>
                                                <FlatButton
                                                    label="Play Card"
                                                    className="PlayCardButton"
                                                    onClick={() => this.playCard(card.id)}
                                                />
                                                <FlatButton
                                                    label="Wonder"
                                                    onClick={() => this.wonderCard(card.id)}
                                                />
                                                <FlatButton
                                                    label="Discard"
                                                    className="DiscardCardButton"
                                                    onClick={() => this.discard(card.id)}
                                                />
                                            </CardActions>
                                        </Card>
                                    );
                                })
                            }
                        </center>
                        </div>
                        <div>
                            <PlayerDisplay playerId={this.props.playerId} />
                        </div>
                        {showPlayCardError &&
                            <Dialog
                                title="You have already played a card this round"
                                actions={showPlayCardActions}
                                open={showPlayCardError}
                                onRequestClose={this.hidePlayCardError}
                            >
                              Please wait for other players to play their card
                            </Dialog>
                        }
                        {showInvalidMoveError &&
                            <Dialog
                                title="Sorry this card is not valid"
                                actions={showInvalidMoveActions}
                                open={showInvalidMoveError}
                                onRequestClose={this.hideInvalidMoveError}
                            >
                              Please play the card differrently or choose another card
                            </Dialog>
                        }
                    </div>
                }
                <div>
                    <div style={{ float: 'left', padding: 20 }}>
                        {!error && !game && !started &&
                          <div>
                              <div id="GC" style={{ width: 500 }}>
                                  <h2> Game creation...</h2>
                              </div>
                              <div style={{ padding: 20 }} >
                                  <h3>Now we wait for players to join your game</h3>
                                  <br />
                                  <p>To start the game, there needs to be:</p>
                                  <ul>
                                    <li>Minumum of 3 players</li>
                                    <li>Maximum of 7 players</li>
                                  </ul>
                                  <br />
                                  <center>
                                      <h4><b>... there are
                                      <b style={{ color: 'red' }}> { this.state.playerCount }</b> players so far.
                                      </b></h4>
                                   </center>
                                  <br />
                                  <center><p>The game will start when all players have clicked ready</p></center>
                                </div>
                            </div>
                        }
                        {!error && !game && !started &&
                            <center>
                                {!this.state.ready
                                  ? <RaisedButton
                                        id="ReadyButton"
                                      label="I am ready"
                                      onClick={() => this.startGame()}
                                  />
                                  :
                                  <div>
                                      <h4><b>Now we wait...</b></h4>
                                      <p><i>(Rome was not built in a day)</i></p>
                                  </div>
                                }
                            </center>
                        }
                        {error &&
                            <p>There was an error</p>
                        }
                    </div>
                    {!game &&
                        <div id="GameScreen" style={{ float: 'right', marginRight: 50 }}>
                            <img width="100%" alt="statue" src={'dist/images/background/statue.jpg'} />
                        </div>
                    }
                </div>
                {loading && !game &&
                    <CircularProgress />
                }
            </div>
        );
    }
}

GameScreen.propTypes = {
    checkGameStatus: PropTypes.func.isRequired,
    startGame: PropTypes.func.isRequired,
    error: PropTypes.bool.isRequired,
    game: PropTypes.object,
    started: PropTypes.bool.isRequired,
    loading: PropTypes.bool.isRequired,
    playerId: PropTypes.number,
    playCard: PropTypes.func,
    cardPlayed: PropTypes.bool.isRequired,
    playerCount: PropTypes.number,
    setPollId: PropTypes.func.isRequired,
    cardValid: PropTypes.bool.isRequired,
    clearInvalidCardError: PropTypes.func.isRequired,
};

GameScreen.defaultProps = {
    game: null,
    playerId: null,
    playerCount: null,
    playCard: null,
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(GameScreen);
