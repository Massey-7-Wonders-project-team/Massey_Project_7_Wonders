import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import * as actionCreators from '../actions/auth';
import { RaisedButton } from 'material-ui';
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

@connect(mapStateToProps, mapDispatchToProps)
class Play extends React.Component { // eslint-disable-line react/prefer-stateless-function

    constructor() {
        super();
        this.state = {
            game: false,
            error: false,
        }
        this.startGame = this.startGame.bind(this);
    }

    startGame() {
        // send request to start game
        const token = localStorage.getItem('token');
        fetch('/api/game/start', {
            method: 'get',
            credentials: 'include',
            headers: {
                'Accept': 'application/json', // eslint-disable-line quote-props
                'Content-Type': 'application/json',
                'Authorization': token,
            },
        })
        .then(response => {
            // do something
            if (response.status === 200) {
                console.log('hello')
                this.setState({
                    game: true,
                    error: false,
                });
            }
            else {
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
        })
    }
    render() {
        const { game, error } = this.state;
        return (
            <div className="col-md-8">
                <h1>Play</h1>
                <hr />
                {error &&
                    <p>There was an error</p>
                }
                {!game &&
                    <RaisedButton
                        label="Start Game"
                        onClick={() => this.startGame()}
                    />
                }
                {game &&
                    <GameScreen />
                }
            </div>
        );
    }
}

export default Play;
