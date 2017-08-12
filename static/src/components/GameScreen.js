import React from 'react';

class GameScreen extends React.Component { // eslint-disable-line react/prefer-stateless-function

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
            if (body.player_id) {
                this.setState({
                    game: true,
                    error: false,
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
    render() {
        return (
            <div className="col-md-8">
                Game screen here
            </div>
        );
    }
}

export default GameScreen;
