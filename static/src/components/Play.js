import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import * as actionCreators from '../actions/auth';

function mapStateToProps(state) {
    return {
        isRegistering: state.auth.isRegistering,
        registerStatusText: state.auth.registerStatusText,
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators(actionCreators, dispatch);
}

export class Play extends React.Component { // eslint-disable-line react/prefer-stateless-function
    render() {
        return (
            <div className="Game col-md-8">
                <h1>Play</h1>
                <hr />
            </div>
        );
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Play);
