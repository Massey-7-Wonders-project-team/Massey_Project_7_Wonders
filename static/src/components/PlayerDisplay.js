import React, { PropTypes, Component } from 'react';
import { CardActions, FlatButton, Card,
    CardHeader, CardText, CardMedia, CardTitle, List,
    Table, TableBody, TableRow, TableRowColumn, Avatar } from 'material-ui';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as actions from '../actions/game';
import Inventory from './Inventory';
import Wonder from './Wonder';
import CardHist from './CardHist';

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

export class PlayerDisplay extends Component {

    constructor(props) {
        super(props);
        this.state = {
            userID: null,
            displayID: null,
            userData: null,
        };
        if (this.props.game) {
            // load passed data
            this.state.userID = this.props.game.player.id;
            this.state.displayID = this.props.game.player.id;
            this.state.userData = this.props.game.player;
            // binding
            this.lookLeft = this.lookLeft.bind(this);
            this.lookRight = this.lookRight.bind(this);
            this.lookUser = this.lookUser.bind(this);
            this.search = this.search.bind(this);
            this.searchHistory = this.searchHistory.bind(this);
        }
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.game.player !== this.state.userData) {
            this.setState({
                userData: nextProps.game.player
            })
        }
    }

    lookLeft() {
        const newDisplayID = this.search().left_id;
        this.setState({
            displayID: newDisplayID,
        });
    }

    lookRight() {
        this.setState({
            displayID: this.search().right_id,
        });
    }

    lookUser() {
        this.setState({
            displayID: this.state.userID,
        });
    }

    search() {
        const nameKey = this.state.displayID;
        var data = {};
        if (nameKey === this.state.userID) {
            data = this.state.userData;
        } else {
            const myArray = this.props.game.allPlayers;
            for (var i = 0; i < myArray.length; i++) {
                if (myArray[i].id === nameKey) {
                    data = myArray[i];
                }
            }
        }
        return data;
    }

    searchHistory() {
        const nameKey = this.state.displayID;
        var data = {};
        const myArray = this.props.game.history;
        for (var i = 0; i < myArray.length; i++) {
            const cardArray = myArray[i][0];
            if (cardArray.playerId === nameKey) {
                data = myArray[i];
            }
        }
        return data;
    }

    render() {
        const boardData = this.search();
        const { error, game, started } = this.props;
        const historyData = this.searchHistory();
        const ListStyle = {
            width: 100,
            paddingTop: 0,
        };
        const inventorycustomColumnStyle = {
            paddingTop: 0, width: 140 };
        let imageName = '';
        if (true) {
            const longCityNameArray = (boardData.wonder).split(' ');
            const city = longCityNameArray.length - 1;
            imageName = longCityNameArray[city].toLowerCase();
        }
        let pName = `Player Name (id:${this.state.displayID})`;  // default profile title
        if (boardData.profile) {
            pName = boardData.profile;  // display profile name if present in returned data
        }
        let homeWonder = false;
        if (boardData.id === this.state.userID) {
            homeWonder = true;
        }

        //overlayContainerStyle={{ paddingBottom: '10%' }}
        return (
            <div style={{ paddingLeft: 100, paddingRight: 100 }}>
                {game && !error && started && boardData &&
                    <div>
                        {
                            <div className="PlayerDisplayBoard">
                                <Table>
                                    <TableBody displayRowCheckbox={false} >
                                        <TableRow selectable={false}>
                                            <TableRowColumn width="50" id="leftNav" >
                                                <img alt="" width="20" src='dist/images/icons/left_arrow.png' onTouchTap={this.lookLeft} />
                                            </TableRowColumn>
                                            <TableRowColumn>
                                                <Card
                                                    expanded={this.state.expanded}
                                                    onExpandChange={this.handleExpandChange}
                                                >
                                                    <CardText id="CardText" style={{ paddingBottom: 0, paddingTop: 0 }}>
                                                        <div>
                                                            <Table>
                                                                <TableBody displayRowCheckbox={false} >
                                                                    <TableRow selectable={false}>
                                                                        <TableRowColumn
                                                                            style={inventorycustomColumnStyle}
                                                                        >
                                                                            <List style={ListStyle}>
                                                                                <Inventory item="wood" amount={boardData.wood} extra={boardData.extra_wood} />
                                                                                <Inventory item="brick" amount={boardData.brick} extra={boardData.extra_brick} />
                                                                                <Inventory item="ore" amount={boardData.ore} extra={boardData.extra_ore} />
                                                                                <Inventory item="stone" amount={boardData.stone} extra={boardData.extra_stone} />
                                                                                <Inventory item="glass" amount={boardData.glass} extra={boardData.extra_glass} />
                                                                                <Inventory item="paper" amount={boardData.paper} extra={boardData.extra_paper} />
                                                                                <Inventory item="cloth" amount={boardData.cloth} extra={boardData.extra_cloth} />
                                                                            </List>
                                                                        </TableRowColumn>
                                                                        <TableRowColumn>
                                                                            <CardMedia
                                                                                style={{ clear: 'left', paddingTop: 10 }}
                                                                                overlay={
                                                                                    <CardTitle
                                                                                        title={boardData.profile}
                                                                                        subtitle={boardData.wonder}
                                                                                        style={{ paddingBottom: 0 }}
                                                                                    >
                                                                                    <Wonder boardData={boardData} />
                                                                                    </CardTitle>
                                                                                }
                                                                                overlayContentStyle={{ background: 'none' }}
                                                                            >
                                                                                <img alt="" src={`dist/images/cities/${imageName}B.png`} />
                                                                            </CardMedia>
                                                                        </TableRowColumn>
                                                                        <TableRowColumn
                                                                            style={inventorycustomColumnStyle}
                                                                        >
                                                                            { !homeWonder ?
                                                                                <FlatButton style={{ align: 'left' }} label="Your Wonder" onTouchTap={this.lookUser} />
                                                                                :
                                                                                <FlatButton label=" " disabled={true} />
                                                                            }

                                                                            <List style={ListStyle}>
                                                                                <Inventory item="vp" amount={boardData.points} extra={-1} />
                                                                                <Inventory item="coin" amount={boardData.money} extra={-1} />
                                                                                <Inventory item={`pyramid-stage${boardData.wonder_level}`} amount={boardData.wonder_level} extra={-1} />
                                                                                <Inventory item="military" amount={boardData.military} extra={-1} />
                                                                                <Inventory item="victoryminus1" amount={boardData.military_loss} extra={-1} />
                                                                            </List>
                                                                        </TableRowColumn>
                                                                    </TableRow>
                                                                </TableBody>
                                                            </Table>
                                                        </div>
                                                    </CardText>
                                                </Card>
                                            </TableRowColumn>
                                            <TableRowColumn width="50" id="rightNav" >
                                              <img alt="" width="20" src='dist/images/icons/right_arrow.png' onTouchTap={this.lookRight} />
                                            </TableRowColumn>
                                        </TableRow>
                                    </TableBody>
                                </Table>
                            </div>

                        }
                        <div style={{ padding: 73, paddingTop: 2, paddingBottom: 2 }} >
                            <Card>
                                <CardHeader
                                    title={`${pName}'s Played Cards`}
                                    actAsExpander={true}
                                    showExpandableButton={true}
                                />
                                <CardText id="played_cards" expandable={true}>
                                    <CardHist history={historyData} />
                                </CardText>
                            </Card>
                        </div>
                    </div>
                }
            </div>
        );
    }
}

PlayerDisplay.propTypes = {
    game: PropTypes.object,
    started: PropTypes.bool.isRequired,
};

PlayerDisplay.defaultProps = {
    game: null,
    playerCount: null,
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(PlayerDisplay);
