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
          for (var i=0; i < myArray.length; i++) {
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
        for (var i=0; i < myArray.length; i++) {
            const cardArray = myArray[i];
            if (cardArray[0].playerId === nameKey) {
                  data = myArray[i];
            }
        }
        return data;
    }

    render() {
        const boardData = this.search();
        const historyData = this.searchHistory();
        const { error, game, started } = this.props;
        const ListStyle = {
            width: 100,
            paddingTop: 0,
        };
        const inventorycustomColumnStyle = {
            paddingTop: 0, width: 100 };
        let imageName = '';
        if (true) {
            const longCityNameArray = (boardData.wonder).split(' ');
            const city = longCityNameArray.length - 1;
            imageName = longCityNameArray[city].toLowerCase();
        }
        let pName = `Player Name (id:${this.state.displayID})`;
        if (boardData.profile) {
            pName = boardData.profile;
        }
        let homeWonder = false;
        if (boardData.id === this.state.userID) {
            homeWonder = true;
        }
<<<<<<< HEAD
=======

>>>>>>> b8d0c62ec23f126d607fdadcd6106baa9c55e721
        return (
            <div>
                {game && !error && started && boardData &&
                    <div>
                        {
                          <div className="PlayerDisplayBoard">
                            <Table>
                              <TableBody displayRowCheckbox={false} >
                                <TableRow selectable={false}>
                                  <TableRowColumn width="50" id="leftNav" >
                                    <input type="image" width="20" src='dist/images/icons/left_arrow.png' onClick={this.lookLeft} />
                                  </TableRowColumn>
                                  <TableRowColumn>
                                    <Card
                                        expanded={this.state.expanded}
                                        onExpandChange={this.handleExpandChange}
                                    >
                                        <CardHeader
                                            id="CardHeader"
                                            title={pName}
                                            subtitle={boardData.wonder}
                                            avatar={<Avatar src={`dist/images/cards/age${game.cards[0].age}.png`} size={55} />}
                                            actAsExpander={true}
                                            showExpandableButton={true}
                                        />
                                        <CardText id="CardText" style={{ paddingBottom: 0, paddingTop: 0 }}>
                                            <div>
                                                <Table>
                                                    <TableBody displayRowCheckbox={false} >
                                                        <TableRow selectable={false}>
                                                            <TableRowColumn
                                                                style={inventorycustomColumnStyle}
                                                            >
                                                                <List style={ListStyle}>
                                                                    <Inventory item="wood" amount={boardData.wood + boardData.extra_wood} />
                                                                    <Inventory item="brick" amount={boardData.brick + boardData.extra_brick} />
                                                                    <Inventory item="ore" amount={boardData.ore + boardData.extra_ore} />
                                                                    <Inventory item="stone" amount={boardData.stone + boardData.extra_stone} />
                                                                    <Inventory item="glass" amount={boardData.glass + boardData.extra_glass} />
                                                                    <Inventory item="paper" amount={boardData.paper + boardData.extra_paper} />
                                                                    <Inventory item="cloth" amount={boardData.cloth + boardData.extra_cloth} />
                                                                </List>
                                                            </TableRowColumn>
                                                            <TableRowColumn>
                                                                <CardActions>
                                                                    { !homeWonder ?
                                                                        <FlatButton label="Back to your Wonder" onClick={this.lookUser} />
                                                                        :
                                                                        <FlatButton label="" disabled={true} />
                                                                    }
                                                                </CardActions>
                                                                <CardMedia>
                                                                    <img alt="" src={`dist/images/cities/${imageName}B.png`} />
                                                                </CardMedia>
                                                                <Wonder data={boardData} />
                                                            </TableRowColumn>
                                                            <TableRowColumn
                                                                style={inventorycustomColumnStyle}
                                                            >
                                                                <List style={ListStyle}>
                                                                    <Inventory item="vp" amount={boardData.points} />
                                                                    <Inventory item="coin" amount={boardData.money} />
                                                                    <Inventory item={`pyramid-stage${boardData.wonder_level}`} amount={boardData.wonder_level} />
                                                                </List>
                                                            </TableRowColumn>
                                                            <TableRowColumn
                                                                style={inventorycustomColumnStyle}
                                                            >
                                                                <List id="buildings" style={ListStyle}>
                                                                    <Inventory item="military" amount={boardData.military} />
                                                                    <Inventory item="victoryminus1" amount={boardData.military_loss} />
                                                                    <Inventory item="cog" amount={boardData.cog} />
                                                                    <Inventory item="tablet" amount={boardData.tablet} />
                                                                    <Inventory item="compass" amount={boardData.compass} />
                                                                </List>
                                                            </TableRowColumn>
                                                        </TableRow>
                                                    </TableBody>
                                                </Table>
                                            </div>
                                        </CardText>
                                        <CardText id="played_cards" expandable={true}>
                                            <CardHist history={historyData} />
                                        </CardText>
                                    </Card>
                                  </TableRowColumn>
                                  <TableRowColumn width="50" id="rightNav" >
                                    <input type="image" width="20" src='dist/images/icons/right_arrow.png' onClick={this.lookRight} />
                                  </TableRowColumn>
                                </TableRow>
                              </TableBody>
                            </Table>
                          </div>
                          }
                    </div>
                }
            </div>
        );
    }
}

PlayerDisplay.propTypes = {
    game: PropTypes.object,
    started: PropTypes.bool.isRequired,
    playerId: PropTypes.number.isRequired,

};

PlayerDisplay.defaultProps = {
    game: null,
    playerCount: null,
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(PlayerDisplay);
