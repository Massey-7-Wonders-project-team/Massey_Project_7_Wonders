import React, { Component } from 'react';
import { RaisedButton } from 'material-ui';
import { browserHistory } from 'react-router';
import EndGameMarkup from './EndGameMarkup';

export class Results extends Component {

    constructor() {
        super();
        this.state = {
            game: null,
            error: false,
        };
        this.playAgain = this.playAgain.bind(this);
        this.goHome = this.goHome.bind(this);
    }

    componentDidMount() {
        const token = localStorage.getItem('token');
        // gets the results from the last game
        fetch('/api/game/result', {
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
            console.log(body)
            // do something
            this.setState({
                game: body.game,
                error: false,
            });
        })
        .catch((err) => {
            // catch error
            console.error(err);
            this.setState({
                data: null,
                error: true,
            });
        });
    }

    playAgain() {
        browserHistory.push('/play');
    }

    goHome() {
        browserHistory.push('/home');
    }

    render() {
        const { game, error } = this.state;

        return (
            <div>
                <div>
                    <h1>Results</h1>
                </div>
                {game && game.allPlayers && !error &&
                    <EndGameMarkup players={game.allPlayers} />
                }
                {error &&
                    <p>There was an error getting your game results</p>
                }
                {
                    <div style={{ paddingTop: '30px' }}>
                        <RaisedButton
                            label="Play Again"
                            style={{
                                marginRight: '20px',
                            }}
                            onClick={() => this.playAgain()}
                        />
                        <RaisedButton
                            label="Go Home"
                            onClick={() => this.goHome()}
                        />
                    </div>

                }
            </div>
        );
    }
}

export default Results;
