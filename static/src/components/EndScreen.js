import React, { PropTypes, Component } from 'react';
import { FlatButton, Dialog, Table, TableBody,
         TableRow, TableRowColumn, TableHeader, tableHeaderColumn } from 'material-ui';
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
            open: false,
        };
        if (this.props.game) {
            this.state.userID = this.props.player.id;
            this.state.userData = this.props.game.player;
            this.state.allPlayers = this.props.game.allPlayers;
            this.getData();
        }
    }

    componentDidMount() {
        console.log('componentDidMount');
    }

    getData() {
        if (this.state.fetch) {
            const token = localStorage.getItem('token');
            fetch(`/api/game/status?player_id=${this.state.displayID}`, {
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
                console.log('getData(body): ', body);

                if (body.game) {
                    this.setState({
                        displayData: body.game.player,
                        Players: body.players,
                        allPlayers: body.game.allPlayers,
                        fetch: false,
                    });
                }
            });
        }
    }

    handleOpen = () => {
        this.setState({ open: true });
    }

    handleClose = () => {
        this.setState({ open: false });
    }

    render() {
        const { error, game, started } = this.props;
        const primary = true;
        const scoreBoardActions = [
            <FlatButton
                label="Close"
                primary={primary}
                onClick={this.handleClose}
            />,
        ];
        const rows = this.state.data.map(player => <PlayerRow key={player} data={player} />);
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
                        <TableHeader>
                            <TableRow>
                                <tableHeaderColumn> ID </tableHeaderColumn>
                                <tableHeaderColumn> Points </tableHeaderColumn>
                                <tableHeaderColumn> Coin </tableHeaderColumn>
                                <tableHeaderColumn> Military </tableHeaderColumn>
                            </TableRow>
                        </TableHeader>
                        <TableBody>{rows}</TableBody>
                    </Table>
                </Dialog>
            </div>
        );
    }
}

const PlayerRow = game =>
    <div>
        <TableRow>
            <TableRowColumn> {game.player.id} </TableRowColumn>
            <TableRowColumn> {game.player.points} </TableRowColumn>
            <TableRowColumn> {game.player.money} </TableRowColumn>
            <TableRowColumn> {game.player.military} </TableRowColumn>
        </TableRow>
        <TableRow>
            <TableRowColumn> {game.allPlayers[0].id} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[0].points} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[0].money} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[0].military} </TableRowColumn>
        </TableRow>
        <TableRow>
            <TableRowColumn> {game.allPlayers[1].id} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[1].points} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[1].money} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[1].military} </TableRowColumn>
        </TableRow>
        <TableRow>
            <TableRowColumn> {game.allPlayers[2].id} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[2].points} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[2].money} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[2].military} </TableRowColumn>
        </TableRow>
        <TableRow>
            <TableRowColumn> {game.allPlayers[3].id} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[3].points} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[3].money} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[3].military} </TableRowColumn>
        </TableRow>
        <TableRow>
            <TableRowColumn> {game.allPlayers[4].id} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[4].points} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[4].money} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[4].military} </TableRowColumn>
        </TableRow>
        <TableRow>
            <TableRowColumn> {game.allPlayers[5].id} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[5].points} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[5].money} </TableRowColumn>
            <TableRowColumn> {game.allPlayers[5].military} </TableRowColumn>
        </TableRow>
    </div>;


EndScreen.propTypes = {
    game: PropTypes.object,
    started: PropTypes.bool.isRequired,
    playerid: PropTypes.number.isRequired,
};

EndScreen.defaultProps = {
    game: null,
    playercount: null,
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(EndScreen);
