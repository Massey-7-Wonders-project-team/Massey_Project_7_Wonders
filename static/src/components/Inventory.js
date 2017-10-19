import React, { PropTypes } from 'react';
import { Chip, Avatar } from 'material-ui';

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
    let showExtra = true;
    if (props.extra < 1) showExtra = false
    return (
        <div>
            {!showExtra ?
                <Chip style={styles.chip}>
                    <Avatar src={`dist/images/icons/${props.item}.png`} />
                    {props.amount.toString()}
                </Chip>
                :
                <Chip style={styles.chip}>
                    <Avatar src={`dist/images/icons/${props.item}.png`} />
                    {props.amount.toString()} / {props.extra.toString()}
                </Chip>
            }
        </div>
    );
}

Inventory.propTypes = {
    amount: PropTypes.number.isRequired,
    item: PropTypes.string.isRequired,
};

export default Inventory;
