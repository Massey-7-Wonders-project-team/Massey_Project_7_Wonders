import React, { PropTypes } from 'react';
import { Table, TableHeader, TableRow, TableBody, TableRowColumn, TableHeaderColumn } from 'material-ui';

const tableFalse = false;
const tableTrue = true;
let allPlayers = [];
let originalPlayerData = null;
let userName = "";

function sortByPoints(a,b) {
    if (a.points > b.points) { return -1; }
    if (a.points < b.points) { return 1; }
    return 0;
}

function EndGameMarkup (props) {
    if(originalPlayerData !== props.players) {
      originalPlayerData = props.players;
      allPlayers = props.players;
      allPlayers.push(props.player);
      allPlayers.sort(sortByPoints);
      userName = props.player.profile;
    }

    return (
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
              {allPlayers.map(player => {
                  if (player.profile === userName) {
                      return (
                      <TableRow key={player.profile} style={{ background: 'red' }}>
                          <TableRowColumn> {player.profile} </TableRowColumn>
                          <TableRowColumn> {player.points} </TableRowColumn>
                          <TableRowColumn> {player.money} </TableRowColumn>
                          <TableRowColumn> {player.military} </TableRowColumn>
                      </TableRow>
                    );
                  } else {
                    return(
                      <TableRow key={player.profile}>
                          <TableRowColumn> {player.profile} </TableRowColumn>
                          <TableRowColumn> {player.points} </TableRowColumn>
                          <TableRowColumn> {player.money} </TableRowColumn>
                          <TableRowColumn> {player.military} </TableRowColumn>
                      </TableRow>
                    )
                  }
              }
              )}
          </TableBody>
      </Table>
    );
}

EndGameMarkup.propTypes = {
    players: PropTypes.array.isRequired,
    player: PropTypes.object.isRequired,
};

export default EndGameMarkup;
