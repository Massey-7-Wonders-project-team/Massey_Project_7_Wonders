import React, { PropTypes } from 'react';
import { Table, TableBody, TableRow, TableRowColumn } from 'material-ui';

function Wonder(props) {
    const boardData = props.data;
    var rows = [];
    for (var each = 0; each < boardData.max_wonder; each ++) {
        if (each < boardData.wonder_level) {
            rows.push('Complete');
        } else {
            rows.push(null);
        }
    }

    return (
        <Table
            id="wonderTable"
            style={{ marginLeft:10, marginRight: 10 }}>
            <TableBody
                displayRowCheckbox={false}
            >
                <TableRow>
                    {
                        rows.map((wCard) => {
                    if (wCard) {
                      return (
                          <TableRowColumn style={{ padding: 0}}>
                          <center>
                                  <img width="150" alt="Complete" src={'dist/images/icons/wonderCard.png'} />
                          </center>
                          </TableRowColumn>
                      );
                    } else {
                      return (
                        <TableRowColumn style={{ padding: 0 }}>

                        </TableRowColumn>
                    )
                    }
                })

              }
            </TableRow>
          </TableBody>
        </Table>
  )
}

Wonder.propTypes = {
    boardData: PropTypes.object.isRequired,
};

export default Wonder;
