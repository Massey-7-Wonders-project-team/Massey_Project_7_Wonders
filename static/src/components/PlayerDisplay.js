import React, { PropTypes, Component } from 'react';
import { CardActions, FlatButton, Card,
    CardHeader, CardText, CardMedia, CardTitle, List,
    Table, TableBody, TableRow, TableRowColumn } from 'material-ui';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as actions from '../actions/game';
import Inventory from './Inventory';

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
            displayData: null,
            fetch: true,
        };
        if (this.props.playerId) {
            this.state.displayID = this.props.playerId;
            this.state.userID = this.props.playerId;
            this.lookLeft = this.lookLeft.bind(this);
            this.lookRight = this.lookRight.bind(this);
            this.lookUser = this.lookUser.bind(this);
            this.getData = this.getData.bind(this);
            this.getData();
        }
    }

    componentDidMount() {
        console.log("CDM");
    }

    getDataLoop() {
      // this function is to loop through current display and both left and right data retrieval
      // need to send props of current, left, right to getData(props)
    }

    getData() {
        if (this.state.fetch) {
            // console.log('GET DATA FUNCTION ACTIVE');
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
                        totalPlayers: body.players,
                        fetch: false,
                    });
                }
            });
        }
    }


    lookLeft() {
        console.log('** CLICKED LEFT **');
        const newDisplayID = this.state.displayData.left_id;
        this.setState({
            displayID: newDisplayID,
            fetch: true,
        });
        this.getData();
    }

    lookRight() {
        console.log('** CLICKED RIGHT **');
        this.setState({
            displayID: this.state.displayData.right_id,
            fetch: true,
        });
        this.getData();
    }

    lookUser() {
        console.log('** CLICKED View User **');
        this.setState({
            displayID: this.state.userID,
            fetch: true,
        });
        this.getData();
    }

    render() {
        const { error, game, started } = this.props;
        const ListStyle = {
            width: 100,
            paddingTop: 0,
        };
        const inventorycustomColumnStyle = {
            paddingTop: 0, width: 100 };
        let imageName = '';
        if (this.state.displayData) {
            const longCityNameArray = (this.state.displayData.wonder).split(' ');
            const city = longCityNameArray.length - 1;
            imageName = longCityNameArray[city].toLowerCase();
        }

        return (
            <div>
                {game && !error && started && this.state.displayData &&
                    <div>
                        {
                          <div>
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
                                            title={`Player Name (id:${this.state.displayID})`}  // "(Add players Name here)"
                                            subtitle={this.state.displayData.wonder}
                                            avatar={`dist/images/cards/age1.png`}               // ${game.cards[0].age}
                                            actAsExpander={true}
                                            showExpandableButton={true}
                                            onChange={this.getData()}
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
                                                                    <Inventory item="wood" amount={this.state.displayData.wood} />
                                                                    <Inventory item="brick" amount={this.state.displayData.brick} />
                                                                    <Inventory item="ore" amount={this.state.displayData.ore} />
                                                                    <Inventory item="stone" amount={this.state.displayData.stone} />
                                                                    <Inventory item="glass" amount={this.state.displayData.glass} />
                                                                    <Inventory item="paper" amount={this.state.displayData.paper} />
                                                                    <Inventory item="cloth" amount={this.state.displayData.cloth} />
                                                                </List>
                                                            </TableRowColumn>
                                                            <TableRowColumn>
                                                                <CardMedia
                                                                    overlay={<CardTitle subtitle="Player thinking..." />}
                                                                >
                                                                    <img alt="" src={`dist/images/cities/${imageName}A.png`} />
                                                                </CardMedia>
                                                                <CardActions>
                                                                        <FlatButton label="Back to your Wonder" onClick={this.lookUser} />
                                                                </CardActions>
                                                            </TableRowColumn>
                                                            <TableRowColumn
                                                                style={inventorycustomColumnStyle}
                                                            >
                                                                <List style={ListStyle}>
                                                                    <Inventory item="vp" amount={this.state.displayData.points} />
                                                                    <Inventory item="coin" amount={this.state.displayData.money} />
                                                                    <Inventory item="pyramid-stage0" amount={this.state.displayData.wonder_level} />
                                                                    <br />
                                                                    <Inventory item="military" amount={this.state.displayData.military} />
                                                                    <Inventory item="victoryminus1" amount='0' />

                                                                </List>
                                                            </TableRowColumn>
                                                            <TableRowColumn
                                                                style={inventorycustomColumnStyle}
                                                            >
                                                                <List id="buildings" style={ListStyle}>
                                                                    <Inventory item="cogs" amount="0" />
                                                                    <Inventory item="script" amount="0" />
                                                                    <Inventory item="compas" amount="0" />
                                                                    <Inventory item="commercial" amount="0" />
                                                                    <Inventory item="civillian" amount="0" />
                                                                </List>
                                                            </TableRowColumn>
                                                        </TableRow>
                                                    </TableBody>
                                                </Table>
                                            </div>
                                        </CardText>
                                        <CardText id="played cards" expandable={true}>
                                            <hr />
                                            <h3>All Cards Played for Wonder</h3>
                                            <p><i>
                                                Card 1, Card 2...
                                            </i></p>
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
                        <hr />
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
