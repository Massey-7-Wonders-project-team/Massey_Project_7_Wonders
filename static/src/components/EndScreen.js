import React, { PropTypes, Component } from 'react';
import { FlatButton, Dialog } from 'material-ui';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as actions from '../actions/game';
import EndGameMarkup from './EndGameMarkup';

function mapStateToProps(state) {
    return {
        game: state.game.game,
        started: state.game.started,
        error: state.game.error,
        loading: state.game.loading,
        playerCount: state.game.playerCount,
        completed: state.game.completed,
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(actions, dispatch);
}

export class EndScreen extends Component {
    constructor(props) {
        super(props);
        this.state = {
            userID: null,
            displayData: null,
            fetch: true,
            selectable: false,
        };
    }

    handleClose = () => {
        this.props.hideScoreboard();
    }

    render() {
        const primaryButton = true;
        const open = true;
        const { game } = this.props;
        const totalPlayers = this.props.game.allPlayers;
        totalPlayers.push(game.player);

        if (this.props.endOfRound) {
            this.handleOpen();
        }
        const scoreBoardActions = [
            <FlatButton
                label="Close"
                primary={primaryButton}
                onClick={this.handleClose}
            />,
        ];

        let title = 'Final Results';
        console.log(game.game)
        if (game.game.age === 2) {
            title = 'Results from Round 1';
        } else if (game.game.age === 3) {
            title = 'Results from Round 2';
        }
        return (
            <div>
                <Dialog
                    title={title}
                    actions={scoreBoardActions}
                    modal={false}
                    open={open}
                    onRequestClose={this.handleClose}
                >
                    <EndGameMarkup players={totalPlayers} />
                </Dialog>
            </div>
        );
    }
}

EndScreen.propTypes = {
    game: PropTypes.object,
    endOfRound: PropTypes.bool.isRequired,
    age: PropTypes.string.isRequired,
    hideScoreboard: PropTypes.func.isRequired,
    endGame: PropTypes.func.isRequired,
};
EndScreen.defaultProps = {
    game: null,
    playercount: null,
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(EndScreen);
