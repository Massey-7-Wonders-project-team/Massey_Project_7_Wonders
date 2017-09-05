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
    return (
        <Chip style={styles.chip}>
            <Avatar src={`dist/images/icons/${props.item}.png`} />
            {props.amount.toString()}
        </Chip>
    );
}

Inventory.propTypes = {
    amount: PropTypes.number.isRequired,
    item: PropTypes.string.isRequired,
};

export default Inventory;
