import React, { PropTypes } from 'react';
import { Table, TableHeader, TableRow, TableBody, TableRowColumn, TableHeaderColumn } from 'material-ui';

const tableFalse = false;
const tableTrue = true;

const EndGameMarkup = props =>
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
            {props.players.map(player =>
                <TableRow key={player.name}>
                    <TableRowColumn> {player.profile} </TableRowColumn>
                    <TableRowColumn> {player.points} </TableRowColumn>
                    <TableRowColumn> {player.money} </TableRowColumn>
                    <TableRowColumn> {player.military} </TableRowColumn>
                </TableRow>,
            )}
        </TableBody>
    </Table>;

EndGameMarkup.propTypes = {
    players: PropTypes.array.isRequired,
};

export default EndGameMarkup;
