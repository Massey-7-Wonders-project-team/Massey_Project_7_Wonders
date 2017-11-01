import React, { PropTypes, Component } from 'react';
import { RaisedButton, IconButton, CardActions, FlatButton, Card,
    CardText, CardMedia, CardTitle, CircularProgress, Dialog } from 'material-ui';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as actions from '../actions/game';
import { poll } from '../utils/misc';
import PlayerDisplay from './PlayerDisplay';
import EndScreen from './EndScreen';
import MilitaryUpdate from './MilitaryUpdate';

function mapStateToProps(state) {
    return {
        game: state.game.game,
        started: state.game.started,
        error: state.game.error,
        loading: state.game.loading,
        playerCount: state.game.playerCount,
        cardPlayed: state.game.cardPlayed,
        cardValid: state.game.cardValid,
        message: state.game.message,
        leftCost: state.game.leftCost,
        rightCost: state.game.rightCost,
        trade: state.game.trade,
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(actions, dispatch);
}

const style = {
    padding: '50px 0',
    margin: '20px auto',
    textAlign: 'center',
    display: 'block',
    overflow: 'hidden',
};


export class GameScreen extends Component {

    constructor() {
        super();
        this.state = {
            polling: false,
            showPlayCardError: false,
            showDiscarded: false,
            pollId: null,
            playerCount: null,
            ready: false,
            endOfRound: false,
            ageDialog: false,
            ageDialogDisplayOnce: false,
            armyDialog: false,
            armyDialogDisplayOnce: false,
            showScoreBoard: false,
            shownForRound: false,
            endGameScoreboard: false,
            showInvalidMoveError: false,
            showTradeDialog: false,
            tradeDialogOnce: false,
            currentPlayingCard: 'Default',
            currentCardID: 0,
            leftCost: 0,
            rightCost: 10,
            trade: false,
            wonderTrade: false,
        };
        this.startGame = this.startGame.bind(this);
        this.pollGameStatus = this.pollGameStatus.bind(this);
        this.hidePlayCardError = this.hidePlayCardError.bind(this);
        this.playersLogged = this.playersLogged.bind(this);
        this.hideScoreboard = this.hideScoreboard.bind(this);
        this.hideInvalidMoveError = this.hideInvalidMoveError.bind(this);
        this.hideAgeDialog = this.hideAgeDialog.bind(this);
        this.hideArmyDialog = this.hideArmyDialog.bind(this);
        this.wonderCard = this.wonderCard.bind(this);
        this.hideDiscarded = this.hideDiscarded.bind(this);
        this.hideTradeDialogPurchase = this.hideTradeDialogPurchase.bind(this);
        this.hideTradeDialogCancel = this.hideTradeDialogCancel.bind(this);
        this.hideTradeDialogPurchaseWonder = this.hideTradeDialogPurchaseWonder.bind(this);
        this.hideTradeDialogCancelWonder = this.hideTradeDialogCancelWonder.bind(this);
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
        if (nextProps.started) {
            this.setState({
                leftCost: nextProps.leftCost,
                rightCost: nextProps.rightCost,
                message: nextProps.message,
            });
            if (nextProps.message !== null) {
                if (nextProps.message.includes("played")) {
                    this.setState({
                        showTradeDialog: false,
                        currentPlayingCard: null,
                        wonderTrade: false,
                    });
                }
            }
            if (nextProps.trade === true && !this.state.tradeDialogOnce &&
              this.state.currentPlayingCard !== null ) {
                this.setState({
                    showTradeDialog: true,
                });
            }
            if (nextProps.cardPlayed) {
                this.setState({
                    showTradeDialog: false,
                    tradeDialogOnce: false,
                });
            }
            if (!this.state.shownForRound &&
                nextProps.game.game.round === 1 && nextProps.game.game.age > 1) {
                this.setState({
                    armyDialog: true,
                });
            }
            if (nextProps.game.game.round === 2) {
                this.setState({
                    shownForRound: false,
                    ageDialogDisplayOnce: false,
                    ageDialog: false,
                    armyDialog: false,
                    armyDialogDisplayOnce: false
                });
            }
            if (nextProps.game.game.round === 1 && nextProps.game.game.age === 1) {
                this.setState({
                    ageDialog: true,
                });
            }
            if (nextProps.game.game.round === 1 && nextProps.game.game.age === 1) {
                this.setState({
                    ageDialog: true,
                });
            }
        }

        if (nextProps.started && !this.state.polling) {
            this.setState({
                polling: true,
            });
            this.pollGameStatus();
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

    // special playCard case for halikarnassos card
    playSpecial(cardId) {
        if (!this.props.cardPlayed) {
            this.props.playCard(this.props.playerId, cardId, false, false, true, true);
            this.setState({
                showDiscarded: false,
            });
        }
    }

    playCard(cardId, cardName) {
        if (!this.props.cardPlayed) {
            this.setState({
                currentPlayingCard: cardName,
                currentCardID: cardId,
                tradeDialogOnce: false,
            });
            this.props.playCard(this.props.playerId, cardId, false, false, false);
        } else {
            this.setState({
                showPlayCardError: true,
            });
        }
    }

    playCardTrade() {
        if (!this.props.cardPlayed) {
            this.setState({
                tradeDialog: false,
            });
            this.props.playCard(this.props.playerId, this.state.currentCardID, false, false, true);
        } else {
            this.setState({
                showPlayCardError: true,
            });
        }
    }

    wonderCard(cardId, cardName) {
        if (!this.props.cardPlayed) {
            this.setState({
                currentPlayingCard: cardName,
                currentCardID: cardId,
                tradeDialogOnce: false,
                wonderTrade: true,
            });
            this.props.playCard(this.props.playerId, cardId, false, true, false);
            if (this.props.game.player.wonder === 'The Mausoleum of Halicarnassus') {
                this.setState({
                    showDiscarded: true,
                });
            }
        } else {
            this.setState({
                showPlayCardError: true,
            });
        }
    }

    wonderCardTrade() {
        if (!this.props.cardPlayed) {
            this.setState({
                tradeDialog: false,
            });
            this.props.playCard(this.props.playerId, this.state.currentCardID, false, true, true);
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
            ageDialog: true,
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

    hideArmyDialog() {
        this.setState({
            armyDialog: false,
            armyDialogDisplayOnce: true,
            showScoreBoard: true,
        });
    }


    hideDiscarded() {
        this.setState({
            showDiscarded: false,
        });
    }


    hideTradeDialogPurchase() {
        this.setState({
            trade: false,
            tradeDialogOnce: true,
        });
        this.playCardTrade();
    }
    hideTradeDialogCancel() {
        this.setState({
            showTradeDialog: false,
            trade: false,
            tradeDialogOnce: true,
        });
    }

    hideTradeDialogPurchaseWonder() {
        this.setState({
            trade: false,
            tradeDialogOnce: true,
        });
        this.wonderCardTrade();
    }
    hideTradeDialogCancelWonder() {
        this.setState({
            showTradeDialog: false,
            trade: false,
            tradeDialogOnce: true,
            wonderTrade: false,
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
        const { error, game, started, loading, message } = this.props;
        const { showPlayCardError, showScoreBoard, showInvalidMoveError, showDiscarded } = this.state;
        const showPlayCardActions = [
            <FlatButton
                label="Ok"
                onTouchTap={this.hidePlayCardError}
            />,
        ];
        const showInvalidMoveActions = [
            <FlatButton
                label="Ok"
                onTouchTap={this.hideInvalidMoveError}
            />,
        ];
        let nextWonderLevel = 1;
        let canPlayWonder = true;
        if (!started) {
            this.playersLogged();
        }
        if (started && game) {
            if (game.game.age) {
                document.title = `Age: ${game.game.age} Round: ${game.game.round}`;
                nextWonderLevel = game.player.wonder_level + 1;
                if (nextWonderLevel > game.player.max_wonder) {
                    canPlayWonder = false;
                }
            }
        }
        const tradeCost = this.state.leftCost + this.state.rightCost;
        let coinArray = [];
        for (var i = 0; i < tradeCost; ++i ) {
            coinArray.push("coin" + i)
        }
        let currentCardImage = '';
        if (this.state.currentPlayingCard !== null ) {
            currentCardImage = (this.state.currentPlayingCard).replace(/\s+/g, '').toLowerCase();
        }

        return (
            <div>
                {game && !error && started &&
                    <div>
                        <div className="GameScreen">
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
                                            onTouchTap={this.hideAgeDialog}
                                        />
                                    }
                                    open={this.state.ageDialog}
                                    onRequestClose={this.hideAgeDialog}
                                    contentStyle={{ width: '40%' }}
                                >
                                    <center><div>
                                        <img alt="Age_image" height='150' src={`dist/images/icons/age${game.game.age}cards.png`} />
                                    </div></center>
                                </Dialog>
                            }
                            {this.state.armyDialog && !this.state.armyDialogDisplayOnce &&
                                <Dialog
                                    id="armyDialog"
                                    title={`Military Updates at end of Age ${game.game.age - 1}`}
                                    actions={
                                        <FlatButton
                                            label="Close"
                                            primary={true}
                                            onClick={this.hideArmyDialog}
                                        />
                                    }
                                    open={this.state.armyDialog}
                                    onRequestClose={this.hideArmyDialog}
                                    contentStyle={{ width: '100%' }}
                                >
                                    <MilitaryUpdate data={this.props.game} />
                                </Dialog>
                            }
                            {this.state.showTradeDialog && !this.state.wonderTrade &&
                                <Dialog
                                    id="tradeDialog"
                                    title={`Confirm Trade`}
                                    actions={[
                                        <FlatButton
                                            label="Cancel trade"
                                            primary={true}
                                            onClick={this.hideTradeDialogCancel}
                                        />,
                                        <FlatButton
                                            label="Purchase Goods"
                                            primary={true}
                                            onClick={this.hideTradeDialogPurchase}
                                        /> ]
                                    }
                                    open={this.state.showTradeDialog}
                                    onRequestClose={this.hideTradeDialog}
                                    contentStyle={{ width: '100%' }}
                                >
                                    <div>
                                        <p style={{ clear: 'left' }}>
                                        To build your <b>{this.state.currentPlayingCard} </b>
                                        you need to pay <b>{tradeCost}</b> Coin for the correct resources</p>
                                    </div>
                                    <div style={{ clear: 'left', float: 'left', align: 'middle', padding: 50 }}>
                                    {
                                          coinArray.map((coin) => {
                                              return (<img key={coin} alt="" src={`dist/images/icons/coin.png`} />);
                                          })
                                    }
                                    </div>
                                    <h1 style={{ float: 'left', width: 120, paddingRight: 30, paddingTop: 32 }}><b>=</b></h1>
                                    <img alt={this.state.currentPlayingCard}
                                        height='150'
                                        src={`dist/images/cards/${currentCardImage}.png`}
                                    />
                                </Dialog>
                            }
                            {this.state.showTradeDialog && this.state.wonderTrade &&
                                <Dialog
                                    id="tradeDialog"
                                    title={`Confirm Trade`}
                                    actions={[
                                        <FlatButton
                                            label="Cancel trade"
                                            primary={true}
                                            onClick={this.hideTradeDialogCancelWonder}
                                        />,
                                        <FlatButton
                                            label="Purchase Goods"
                                            primary={true}
                                            onClick={this.hideTradeDialogPurchaseWonder}
                                        /> ]
                                    }
                                    open={this.state.showTradeDialog}
                                    onRequestClose={this.hideTradeDialog}
                                    contentStyle={{ width: '100%' }}
                                >
                                    <div>
                                        <p style={{ clear: 'left' }}>
                                        To build your <b>Stage {`${this.props.game.player.wonder_level + 1}`} Wonder </b>
                                        you need to pay <b>{tradeCost}</b> Coin for the correct resources</p>
                                    </div>
                                    <div style={{ clear: 'left', float: 'left', align: 'middle', padding: 50 }}>
                                    {
                                          coinArray.map((coin) => {
                                              return (<img key={coin} alt="" src={`dist/images/icons/coin.png`} />);
                                          })
                                    }
                                    </div>
                                    <h1 style={{ float: 'left', width: 120, paddingRight: 30, paddingTop: 32 }}><b>=</b></h1>
                                    <img alt={this.props.game.player.wonder_level + 1}
                                        height='100'
                                        src={`dist/images/icons/pyramid-stage${this.props.game.player.wonder_level + 1}.png`}
                                        style={{ paddingTop: 20, paddingLeft: 0 }}
                                    />
                                </Dialog>
                            }
                            <div>
                                {showScoreBoard &&
                                    <EndScreen
                                        hideScoreboard={this.hideScoreboard}
                                        endGameScoreboard={this.state.endGameScoreboard}
                                        currentScore={this.props.game}
                                    />
                                }
                            </div>
                            <center>
                                {game.cards &&
                                  game.cards.map((card, index) => {
                                      const imageName = (card.name).replace(/\s+/g, '').toLowerCase();
                                      return (
                                          <Card className="Card" data-card-number={index} key={card.id} style={{ marginRight: 5, width: 130, display: 'inline-block', paddingBottom: 0 }}>
                                              <CardMedia>
                                                  <img
                                                      alt={`${card.name} image`}
                                                      src={`dist/images/cards/${imageName}.png`}
                                                      width="120"
                                                      title={`${card.name}`}
                                                      onTouchTap={() => this.playCard(card.id)}
                                                  />
                                              </CardMedia>
                                              <CardActions style={{ padding: 0, backgroundColor: 'lightblue' }}>
                                                  <IconButton style={{ width: 30 }} tooltip={`Play ${card.name}`} touch={true} tooltipPosition="bottom-center">
                                                      <img width="18" src={`dist/images/icons/check.png`} onTouchTap={() => this.playCard(card.id)} />
                                                  </IconButton>
                                                  { canPlayWonder &&
                                                      <IconButton style={{ width: 39 }} tooltip="Play for Wonder" touch={true} tooltipPosition="bottom-center">
                                                          <center><img width="30" src={`dist/images/icons/pyramid-stage${nextWonderLevel}.png`} onTouchTap={() => this.wonderCard(card.id)} /></center>
                                                      </IconButton>
                                                  }
                                                  <IconButton style={{ width: 30 }} tooltip={`Discard ${card.name}`} touch={true} tooltipPosition="bottom-center">
                                                      <img width="20" src={`dist/images/icons/trash.png`} onTouchTap={() => this.discard(card.id)} />
                                                  </IconButton>
                                              </CardActions>
                                          </Card>
                                      );
                                  })
                              }
                            </center>
                            <center>
                                {showDiscarded &&
                                <Dialog
                                    id="discardDialog"
                                    title="Play a card from the discard pile..."
                                    open={showDiscarded}
                                    onRequestClose={this.hideDiscarded}
                                    autoScrollBodyContent={true}
                                    actions={
                                        <FlatButton
                                            label="Close"
                                            primary={true}
                                            onClick={this.hideDiscarded}
                                        />}
                                >
                                    {game.discarded &&
                                    game.discarded.map((card, index) => {
                                        const imageName = (card.name).replace(/\s+/g, '').toLowerCase();
                                        return (
                                            <Card className="Card" data-card-number={index} key={card.id} style={{ marginRight: 5, width: 130, display: 'inline-block', paddingBottom: 0 }}>
                                                <CardMedia>
                                                    <img
                                                        alt={`${card.name} image`}
                                                        src={`dist/images/cards/${imageName}.png`}
                                                        width="120"
                                                        title={`${card.name}`}
                                                        onTouchTap={() => this.playSpecial(card.id)}
                                                    />
                                                </CardMedia>
                                                <CardActions style={{ padding: 0, backgroundColor: 'lightblue' }}>
                                                    <IconButton style={{ width: 30 }} tooltip={`Play ${card.name} (free)`} touch={true} tooltipPosition="bottom-center">
                                                        <img width="18" src={`dist/images/icons/check.png`} onTouchTap={() => this.playSpecial(card.id)} />
                                                    </IconButton>
                                                </CardActions>
                                            </Card>
                                        );
                                    })
                                    }
                                </Dialog>
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
                                {this.props.message}
                            </Dialog>
                        }
                    </div>
                }
                <div>
                    <div style={{ float: 'left', padding: 20 }}>
                        {!error && !game && !started &&
                          <div style={style}>
                              <div id="GC">
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
                                      onTouchTap={() => this.startGame()}
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
    cardPlayed: PropTypes.bool,
    playerCount: PropTypes.number,
    setPollId: PropTypes.func.isRequired,
    cardValid: PropTypes.bool,
    clearInvalidCardError: PropTypes.func.isRequired,
    rightCost: PropTypes.number,
    leftCost: PropTypes.number,
    message: PropTypes.string,
    trade: PropTypes.bool,
};

GameScreen.defaultProps = {
    game: null,
    playerId: null,
    playerCount: null,
    playCard: null,
    cardPlayed: null,
    cardValid: null,
    rightCost: null,
    leftCost: null,
    message: null,
    trade: null,
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(GameScreen);
