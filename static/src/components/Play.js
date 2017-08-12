import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { RaisedButton } from 'material-ui';
import * as actionCreators from '../actions/auth';
import GameScreen from './GameScreen';

function mapStateToProps(state) {
    return {
        isRegistering: state.auth.isRegistering,
        registerStatusText: state.auth.registerStatusText,
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(actionCreators, dispatch);
}

// we must export the class for testing. Then also default export the class
// at the end of the file which is used for the actual production render
export class Play extends React.Component {

    constructor() {
        super();
        this.state = {
            game: false,
            error: false,
            gameId: null,
        };
        this.createGame = this.createGame.bind(this);
    }

    componentDidMount() {
        // check if the user is already part of a game
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
            if (body.game_id) {
                this.setState({
                    game: true,
                    error: false,
                    gameId: body.game_id,
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
            this.setState({
                game: true,
                error: false,
            });
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
        const { game, error, gameId } = this.state;
        return (
            <div className="Game col-md-8">
                <h1>Play</h1>
                <hr />
                {error &&
                    <p>There was an error</p>
                }
                {!game &&
                    <RaisedButton
                        label="Create Game"
                        onClick={() => this.createGame()}
                    />
                }
                {game &&
                    <GameScreen gameId={gameId} />
                }
            </div>
        );
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Play);
