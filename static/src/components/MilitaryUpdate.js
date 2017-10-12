import React, { PropTypes } from 'react';
import { Card, CardMedia, CardText } from 'material-ui';

function search(searchID, allPlayers) {
    const myArray = allPlayers;
    for (var i = 0; i < myArray.length; i++) {
        if (myArray[i].id === searchID) {
            return myArray[i];
        }
    }
    return null;
}

function getNeighbourArmy(allData) {
    const userArmy = allData.player;
    const leftArmy = search(allData.player.left_id, allData.allPlayers);
    const rightArmy = search(allData.player.right_id, allData.allPlayers);
    return {
        militaryLevel: [leftArmy.military, userArmy.military, rightArmy.military],
        militaryUsers: [leftArmy.profile, userArmy.profile, rightArmy.profile]
    };
}

function MilitaryUpdate(props) {
    const militaryData = getNeighbourArmy(props.data);
    const levels = militaryData.militaryLevel;
    const names = militaryData.militaryUsers;
    let age = 3;
    if (!props.data.game.clearInterval) { age = props.data.game.age - 1; }
    let lArmy = [];
    for (var each = 0; each < levels[0]; each ++) {
        lArmy.push('militaryUnit');
    }
    let uArmy = [];
    for (var each = 0; each < levels[1]; each ++) {
        uArmy.push('militaryUnit');
    }
    let rArmy = [];
    for (var each = 0; each < levels[2]; each ++) {
        rArmy.push('militaryUnit');
    }

    let winLeft = false;
    let winRight = false;
    let evenLeft = false;
    let evenRight = false;
    if (levels[0] < levels[1]) { winLeft = true; }
    if (levels[1] > levels[2]) { winRight = true; }
    if (levels[0] === levels[1]) { evenLeft = true; }
    if (levels[1] === levels[2]) { evenRight = true; }

    let winImage = 1;
    if (age === 2) { winImage = 3; }
    if (age === 3) { winImage = 5; }

    return (
        <div style={{ width: '100%' }}>
            <center>
                <Card style={{ width: 130, height: '30%', display: 'inline-block', float: 'left' }}>
                    <CardMedia>
                        <div style={{ padding: 15, height: 100 }}>
                            <center>
                                {
                                  lArmy.map((level) => {
                                      return (
                                          <img width="30px" alt={level} src={`dist/images/icons/military.png`} />
                                      );
                                  })
                                }
                            </center>
                        </div>
                    </CardMedia>
                    <CardText>
                        <h4><center>{names[0]}</center></h4>
                    </CardText>
                </Card>
                <div style={{ width: 170, float: 'left', padding: 50 }}>
                    { !evenLeft ?
                        <div>
                            { winLeft ?
                                    <div>
                                        <img alt={`${winImage}VP`} src={`dist/images/icons/victory${winImage}.png`} />
                                    </div>
                                    :
                                    <div>
                                        <img alt="-1VP" src={`dist/images/icons/victoryminus1.png`} />
                                    </div>
                            }
                        </div>
                        :
                        <div>
                            <h1><b>&#61;</b></h1>
                        </div>
                    }
                </div>
                <Card style={{ width: 130, height: '30%', display: 'inline-block', float: 'left' }}>
                    <CardMedia>
                        <div style={{ padding: 15, height: 100  }}>
                            <center>
                                {
                                  uArmy.map((level) => {
                                      return (
                                          <img width="30px" alt={level} src={`dist/images/icons/military.png`} />
                                      );
                                  })
                                }
                            </center>
                        </div>
                    </CardMedia>
                    <CardText>
                        <h4><center><b>Your Military</b></center></h4>
                    </CardText>
                </Card>
                <div style={{ width: 130, float: 'left', padding: 50 }}>
                    { !evenRight ?
                        <div>
                            { winRight ?
                                <div>
                                    <img alt={`${winImage}VP`} src={`dist/images/icons/victory${winImage}.png`} />
                                </div>
                                :
                                <div>
                                    <img alt="-1VP" src={`dist/images/icons/victoryminus1.png`} />
                                </div>
                            }
                        </div>
                        :
                        <div>
                            <h1><b>&#61;</b></h1>
                        </div>
                    }
                </div>
                <Card style={{ width: 130, height: '30%', display: 'inline-block', float: 'left' }}>
                    <CardMedia>
                        <div style={{ padding: 15, height: 100 }}>
                            <center>
                                {
                                  rArmy.map((level) => {
                                      return (
                                          <img width="30px" alt={level} src={`dist/images/icons/military.png`} />
                                      );
                                  })
                                }
                            </center>
                        </div>
                    </CardMedia>
                    <CardText>
                        <h4><center>{names[2]}</center></h4>
                    </CardText>
                </Card>
            </center>
        </div>
    )
}

MilitaryUpdate.propTypes = {
    data: PropTypes.object.isRequired,
};

export default MilitaryUpdate;
