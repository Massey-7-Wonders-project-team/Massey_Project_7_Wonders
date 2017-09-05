import React, { PropTypes, Component } from 'react';
import { RaisedButton, CardActions, FlatButton, Card, CardHeader, CardText, CardMedia, CardTitle } from 'material-ui';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { List } from 'material-ui/List';
import Avatar from 'material-ui/Avatar';
//import Subheader from 'material-ui/Subheader';
import Chip from 'material-ui/Chip';
import {
  Table,
  TableBody,
  TableRow,
  TableRowColumn,
} from 'material-ui/Table';
import * as actions from '../actions/game';

class CardExampleControlled extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      expanded: false,
    };
  }

  handleExpandChange = (expanded) => {
    this.setState({expanded: expanded});
  };

  handleToggle = (event, toggle) => {
    this.setState({expanded: toggle});
  };

  handleExpand = () => {
    this.setState({expanded: true});
  };

  handleReduce = () => {
    this.setState({expanded: false});
  };
}


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
            displayID: null,
            displayData: null,
            userID: null,
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
              console.log('body', body);
              const newDisplayData = body.game.player;
              this.setState({
                  displayData: newDisplayData,
                  fetch: false,
              });
          });
        }
    }


    lookLeft() {
        console.log('** CLICKED LEFT **')
        const newDisplayID = this.state.displayData.left_id;
        this.setState({
            displayID: newDisplayID,
            fetch: true,
        });
        this.getData();
    }

    lookRight() {
        console.log('** CLICKED RIGHT **')
        const newDisplayID = this.state.displayData.right_id;
        this.setState({
            displayID: newDisplayID,
            fetch: true,
        });
        this.getData();
    }

    lookUser() {
        console.log('** CLICKED View User **')
        const newDisplayID = this.state.userID;
        this.setState({
            displayID: newDisplayID,
            fetch: true,
        });
        this.getData();
    }

    render() {
        const { error, game, started, playerCount } = this.props;
        const ListStyle = { width: 100 };
        const inventorycustomColumnStyle = { padding: 0, width: 100 };

        const longCityNameArray = (this.state.displayData.wonder).split(' ');
        const city = longCityNameArray.length - 1;
        const imageName = longCityNameArray[city].toLowerCase();
        console.log("imageName: ",imageName);

        // when cards are generating substitute this code >>   ${game.cards[0].age}

        return (
            <div>
                {game && !error && started &&
                    <div>
                        {
                            <Card
                                expanded={this.state.expanded}
                                onExpandChange={this.handleExpandChange}
                            >
                                <CardHeader
                                    title={`Player Name (id:${this.state.displayID})`}  // "(Add players Name here)"
                                    subtitle={this.state.displayData.wonder}
                                    avatar={`dist/images/cards/age1.png`}
                                    actAsExpander={true}
                                    showExpandableButton={true}
                                    onChange={this.getData()}
                                />
                                <CardText>
                                    <div>
                                        <Table>
                                            <TableBody displayRowCheckbox={false}>
                                                <TableRow>
                                                    <TableRowColumn
                                                        style={inventorycustomColumnStyle}
                                                    >
                                                        <List innerDivStyle={ListStyle}>
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
                                                        <div id="building_stats">
                                                            <Table>
                                                                <TableBody
                                                                    displayRowCheckbox={false}
                                                                >
                                                                    <TableRow>
                                                                        <TableRowColumn>
                                                                            <Inventory item="cogs" amount="0" />
                                                                        </TableRowColumn>
                                                                        <TableRowColumn>
                                                                            <Inventory item="script" amount="0" />
                                                                        </TableRowColumn>
                                                                        <TableRowColumn>
                                                                            <Inventory item="compas" amount="0" />
                                                                        </TableRowColumn>
                                                                        <TableRowColumn>
                                                                            <Inventory item="commercial" amount="0" />
                                                                        </TableRowColumn>
                                                                        <TableRowColumn>
                                                                            <Inventory item="civillian" amount="0" />
                                                                        </TableRowColumn>
                                                                    </TableRow>
                                                                </TableBody>
                                                            </Table>
                                                        </div>

                                                    </TableRowColumn>
                                                    <TableRowColumn
                                                        style={inventorycustomColumnStyle}
                                                    >
                                                        <List innerDivStyle={ListStyle}>
                                                            <Inventory item="vp" amount={this.state.displayData.points} />
                                                            <Inventory item="coin" amount={this.state.displayData.money} />
                                                            <hr />
                                                            <Inventory item="military" amount={this.state.displayData.military} />
                                                            <Inventory item="pyramid-stage0" amount={this.state.displayData.wonder_level} />
                                                        </List>
                                                    </TableRowColumn>
                                                </TableRow>
                                            </TableBody>
                                        </Table>
                                        <hr />
                                        <CardActions>
                                            <center>
                                                <FlatButton label="<< View Left Player" onClick={this.lookLeft} />
                                                <FlatButton label="Back to your Wonder" onClick={this.lookUser} />
                                                <FlatButton label="View Right Player >>" onClick={this.lookRight} />
                                            </center>
                                        </CardActions>
                                    </div>
                                </CardText>
                                <CardText id="played cards" expandable={true}>
                                    <hr />
                                    <h3>All Cards Played for Wonder</h3>
                                    <p><i>
                                        This will be where we place all played cards for current user
                                    </i></p>
                                </CardText>

                            </Card>
                          }
                        <hr />
                    </div>

                }
                {!error && !game && !started &&
                    <RaisedButton
                        label="I am ready"
                        onClick={() => this.startGame()}
                    />
                }
                {!error && !game &&
                    <p>Waiting on more players... {this.state.game.playerCount} players so far.</p>
                }
                {error &&
                    <p>There was an error</p>
                }
            </div>
        );
    }
}

const styles = {
    chip: {
        margin: 4,
    },
    wrapper: {
        display: 'flex',
        flexWrap: 'wrap',
    },
};

function Inventory(props) {
    return (
        <Chip style={styles.chip}>
            <Avatar src={`dist/images/icons/${props.item}.png`} />
            {props.amount.toString()}
        </Chip>
    )
}

PlayerDisplay.propTypes = {
    checkGameStatus: PropTypes.func.isRequired,
    startGame: PropTypes.func.isRequired,
    error: PropTypes.bool.isRequired,
    game: PropTypes.object,
    started: PropTypes.bool.isRequired,
    loading: PropTypes.bool.isRequired,
    playerId: PropTypes.number,
    playerCount: PropTypes.number,
};

export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(PlayerDisplay);
