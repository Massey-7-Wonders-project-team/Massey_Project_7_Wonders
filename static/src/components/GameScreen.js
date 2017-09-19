import React, { PropTypes, Component } from 'react';
import { RaisedButton, CardActions, FlatButton, Card,
    CardText, CardMedia, CardTitle, CircularProgress, Dialog } from 'material-ui';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as actions from '../actions/game';
import { poll } from '../utils/misc';
import PlayerDisplay from './PlayerDisplay';
import EndScreen from "./EndScreen";

function mapStateToProps(state) {
    return {
        game: state.game.game,
        started: state.game.started,
        error: state.game.error,
        loading: state.game.loading,
        playerCount: state.game.playerCount,
        cardPlayed: state.game.cardPlayed,
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
            playerCount: null,
            ready: false,
            endOfRound: false,
        };
        this.startGame = this.startGame.bind(this);
        this.pollGameStatus = this.pollGameStatus.bind(this);
        this.hidePlayCardError = this.hidePlayCardError.bind(this);
        this.playersLogged = this.playersLogged.bind(this);
    }

    componentDidMount() {
        this.props.checkGameStatus(this.props.playerId);
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.started && !this.state.polling) {
            this.setState({
                polling: true,
            });
            this.pollGameStatus();
        }
    }

    pollGameStatus() {
        poll(() => this.props.checkGameStatus(this.props.playerId), 5000);
        console.log("POLLING from gamescreen");
    }

    startGame() {
        if (!this.state.ready) {
            this.setState({
                ready: true,
            })
        }
        this.props.startGame(this.props.playerId);
    }

    playCard(cardId) {
        if (!this.props.cardPlayed) {
            this.props.playCard(this.props.playerId, cardId, false);
        } else {
            this.setState({
                showPlayCardError: true,
            });
        }
    }

    discard(cardId) {
        if (!this.props.cardPlayed) {
            this.props.playCard(this.props.playerId, cardId, true);
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

    playersLogged() {
      // this function is just to find how many players are logged into
      // the currently created game
      // Replication of what Game.js does
      // Just not sure how to retrieve info from Game.js
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
          console.log("PlayersLogged: ", this.state.playerCount);
      });
    }

    render() {
        const { error, game, started, loading, playerCount, endOfRound } = this.props;
        const { showPlayCardError } = this.state;
        let minumum = false;
        if (this.state.playerCount > 2) { minumum = true; }

        const showPlayCardActions = [
            <FlatButton
                label="Ok"
                onClick={this.hidePlayCardError}
            />,
        ];
        // update total numbers of players logged in
        if (!started) {
            this.playersLogged();
        }

        return (
            <div>
                {game && !error && started &&
                    <div>
                        <div>
                            <PlayerDisplay playerId={this.props.playerId} />
                        </div>
                        <div>
                            {endOfRound &&
                                <div>
                                    <EndScreen playerId={this.props.playerId}/>
                                </div>
                          }
                        </div>
                        <div>
                            {game.playedCards &&
                                game.playedCards.map((pcard) => {
                                    const imageName = (pcard.card.name).replace(/\s+/g, '').toLowerCase();
                                    return (
                                        <Card key={pcard.id} style={{ width: 150, display: 'inline-block' }}>
                                            <CardTitle title={pcard.card.name} />
                                            <CardMedia>
                                                <img
                                                    alt={`${pcard.card.name} image`}
                                                    src={`dist/images/cards/${imageName}.png`}
                                                />
                                            </CardMedia>
                                        </Card>
                                    );
                                })
                            }
                            {game.cards && game.cards[0].name &&
                                game.cards.map((card) => {
                                    const imageName = (card.name).replace(/\s+/g, '').toLowerCase();
                                    return (
                                        <Card key={card.id} style={{ width: 150, display: 'inline-block', paddingBottom: 0 }}>
                                            <CardTitle title={card.name} titleStyle={{ fontSize: 18 }} />
                                            <CardMedia>
                                                <img
                                                    alt={`${card.name} image`}
                                                    src={`dist/images/cards/${imageName}.png`}
                                                />
                                            </CardMedia>
                                            <CardText>
                                                <p>Discription of what card does</p>
                                            </CardText>
                                            <CardActions>
                                                <FlatButton
                                                    label="Play Card"
                                                    onClick={() => this.playCard(card.id)}
                                                />
                                                <FlatButton
                                                    label="Discard"
                                                    onClick={() => this.discard(card.id)}
                                                />
                                            </CardActions>
                                        </Card>
                                    );
                                })
                            }
                        </div>
                        {showPlayCardError &&
                            <Dialog
                                title="You have already played a card this round"
                                actions={showPlayCardActions}
                                open={showPlayCardError}
                                onRequestClose={this.hidePlayCardError}
                            >
                              Please what for other players to play their card
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
    endOfRound: PropTypes.bool.isRequired,
    loading: PropTypes.bool.isRequired,
    playerId: PropTypes.number,
    playCard: PropTypes.func,
    cardPlayed: PropTypes.bool.isRequired,
    playerCount: PropTypes.number,
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
