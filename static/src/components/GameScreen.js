import React from 'react';
import { RaisedButton, CardActions, FlatButton, Card, CardText, CardMedia, CardTitle } from 'material-ui';

export class GameScreen extends React.Component {

    constructor() {
        super();
        this.state = {
            error: false,
            playerId: null,
            game: null,
            started: false,
        };
        this.startGame = this.startGame.bind(this);
    }

    componentDidMount() {
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
            // do something
            console.log(body);
            if (body.status === 'Started') {
                this.setState({
                    error: false,
                    game: body.game,
                    playerId: this.props.playerId,
                    started: true,
                });
            } else {
                this.setState({
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

    startGame() {
        const token = localStorage.getItem('token');
        fetch(`/api/game/start?player_id=${this.props.playerId}`, {
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
            if (body.game) {
                this.setState({
                    error: false,
                    game: body.game,
                    started: true,

                });
            } else {
                this.setState({
                    error: false,
                    game: false,
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

    render() {
        const { error, game, started } = this.state;
        return (
            <div>
                {game && !error && started &&
                    <div>
                        {
                            game.cards.map((card) => {
                                console.log(card);
                                const imageName = (card.card.name).replace(/\s+/g, '').toLowerCase();
                                return (
                                    <Card key={card.id} style={{ display: 'inline-block' }}>
                                        <CardTitle title={card.card.name} />
                                        <CardMedia>
                                            <img alt="" src={`/images/cards/${imageName}.png`} />
                                        </CardMedia>
                                        <CardText>
                                            <p>Discription of what card does</p>
                                        </CardText>
                                        <CardActions>
                                            <FlatButton label="Play Card" />
                                            <FlatButton label="Discard" />
                                        </CardActions>
                                    </Card>
                                );
                            })
                        }
                    </div>
                }
                {!error && !game && !started &&
                    <RaisedButton
                        label="I am ready"
                        onClick={() => this.startGame()}
                    />
                }
                {!error && !game &&
                    <p>Waiting on more players...</p>
                }
                {error &&
                    <p>There was an error</p>
                }
            </div>
        );
    }
}

export default GameScreen;
