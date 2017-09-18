import React, { PropTypes, Component } from 'react';
import { RaisedButton, CardActions, FlatButton, Card,
    CardText, CardMedia, CardTitle, CircularProgress, Dialog } from 'material-ui';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as actions from '../actions/game';
import { poll } from '../utils/misc';
import PlayerDisplay from './PlayerDisplay';

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
            pollId: null,
        };
        this.startGame = this.startGame.bind(this);
        this.pollGameStatus = this.pollGameStatus.bind(this);
        this.hidePlayCardError = this.hidePlayCardError.bind(this);
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
        const pollId = poll(() => this.props.checkGameStatus(this.props.playerId), 5000);
        this.props.setPollId(pollId);
    }

    startGame() {
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

    render() {
        const { error, game, started, loading, playerCount } = this.props;
        const { showPlayCardError } = this.state;

        const showPlayCardActions = [
            <FlatButton
                label="Ok"
                onClick={this.hidePlayCardError}
            />,
        ];


        return (
            <div>
                {loading && !game &&
                    <CircularProgress />
                }
                {game && !error && started &&
                    <div>
                        <div>
                            <PlayerDisplay playerId={game.player.id} />
                        </div>
                        <div>
                            {game.playedCards &&
                                game.playedCards.map((pcard) => {
                                    const imageName = (pcard.card.name).replace(/\s+/g, '').toLowerCase();
                                    return (
                                        <Card key={pcard.id} style={{ display: 'inline-block' }}>
                                            <CardTitle title={pcard.card.name} />
                                            <CardMedia>
                                                <img alt="" src={`dist/images/cards/${imageName}.png`} />
                                            </CardMedia>
                                        </Card>
                                    );
                                })
                            }
                            {game.cards &&
                                game.cards.map((card) => {
                                    const imageName = (card.name).replace(/\s+/g, '').toLowerCase();
                                    return (
                                        <Card key={card.id} style={{ display: 'inline-block' }}>
                                            <CardTitle title={card.name} />
                                            <CardMedia>
                                                <img alt="" src={`dist/images/cards/${imageName}.png`} />
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
                    <div style={{ float: 'left', padding: 100 }}>
                        {!error && !game && !started &&
                            <RaisedButton
                                label="I am ready"
                                onClick={() => this.startGame()}
                            />
                        }
                        {!error && !game &&
                            <div style={{ padding: '50' }} >

                              <p>Waiting on more players... <i id="number">{ playerCount }</i> players so far.</p>
                            </div>
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
