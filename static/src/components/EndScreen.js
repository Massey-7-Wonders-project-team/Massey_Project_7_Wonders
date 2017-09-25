import React, { PropTypes, Component } from 'react';
import { FlatButton, Dialog, Table, TableBody,
         TableRow, TableRowColumn, TableHeaderColumn, TableHeader } from 'material-ui';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as actions from '../actions/game';

function mapStateToProps(state) {
    return {
        game: state.game.game,
        started: state.game.started,
        error: state.game.error,
        loading: state.game.loading,
        playerCount: state.game.playerCount,
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
            open: true,
            selectable: false,
            endOfRound: false,
        };
        if (this.props.game) {
            this.state.userData = this.props.game.player;
            this.state.displayData = this.props.game.allPlayers;
            this.state.endOfRound = this.props.endOfRound;
        }
    }

    handleOpen = () => {
        this.setState({ open: true });
    }

    handleClose = () => {
        this.setState({ open: false });
    }
    render() {
        const tableFalse = false;
        const tableTrue = true;
        const user = this.state.userData;
        const players = this.state.displayData;
        const items = players.concat(user);
        if (this.props.endOfRound) {
            this.handleOpen();
        }
        const scoreBoardActions = [
            <FlatButton
                label="Close"
                primary={true}
                onClick={this.handleClose}
            />,
        ];
        return (
            <div>
                <Dialog
                    title="Score Board"
                    actions={scoreBoardActions}
                    modal={false}
                    open={this.state.open}
                    onRequestClose={this.handleClose}
                >
                    <Table>
                        <TableHeader
                            displaySelectALl={tableFalse}
                            endableSelectAll={tableFalse}
                            displayRowCheckbox={tableFalse}
                        >
                            <TableRow>
                                <TableHeaderColumn>Name</TableHeaderColumn>
                                <TableHeaderColumn>Points</TableHeaderColumn>
                                <TableHeaderColumn>Coin</TableHeaderColumn>
                                <TableHeaderColumn>Military</TableHeaderColumn>
                            </TableRow>
                        </TableHeader>
                        <TableBody
                            displayRowCheckbox={tableFalse}
                            showRowHover={tableFalse}
                            stripedRows={tableTrue}
                        >
                            {items.map(player =>
                                <TableRow key={player.id}>
                                    <TableRowColumn> {player.profile} </TableRowColumn>
                                    <TableRowColumn> {player.points} </TableRowColumn>
                                    <TableRowColumn> {player.money} </TableRowColumn>
                                    <TableRowColumn> {player.military} </TableRowColumn>
                                </TableRow>
                            )}
                        </TableBody>
                    </Table>
                </Dialog>
            </div>
        );
    }
}

EndScreen.propTypes = {
    game: PropTypes.object,
    endOfRound: PropTypes.bool.isRequired,
};
EndScreen.defaultProps = {
    game: null,
    playercount: null,
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(EndScreen);
