import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { Paper, FlatButton } from 'material-ui';
import * as actionCreators from '../actions/data';

function mapStateToProps(state) {
    return {
        data: state.data,
        token: state.auth.token,
        loaded: state.data.loaded,
        isFetching: state.data.isFetching,
    };
}


function mapDispatchToProps(dispatch) {
    return bindActionCreators(actionCreators, dispatch);
}

const style = {
    marginTop: 50,
    paddingBottom: 50,
    paddingTop: 25,
    marginLeft: 100,
    width: 300,
    textAlign: 'center',
    display: 'inline-block',
};

export class ProtectedView extends React.Component {
    componentDidMount() {
        this.fetchData();
    }


    fetchData() {
        const token = this.props.token;
        this.props.fetchProtectedData(token);
    }

    render() {
        const Name = (this.props.userName).split('@')[0];
        return (
            <div>
                {!this.props.loaded
                    ? <h1>Loading data...</h1>
                    :
                    <div>
                        <div style={{ float: "left" }}>
                            <h1>Welcome</h1>
                            <Paper style={style} >
                                <h1>&nbsp;&nbsp;{ Name }!</h1>
                                <h3><i>&nbsp;&nbsp;({this.props.data.data.email})</i></h3>
                            </Paper>
                            <br />
                            <FlatButton
                                style={{ marginLeft: 55, marginTop: 25 }}
                                label="Select Play in the Menu to find a Game to join"
                                onTouchTap={() => this.dispatchNewRoute('/play')}
                            />
                        </div>
                        <div style={{ float: 'right', paddingRight: 50 }}>
                            <img alt="statue" src={'dist/images/background/statue.jpg'} />
                        </div>
                    </div>
                }
            </div>
        );
    }
}

ProtectedView.propTypes = {
    fetchProtectedData: React.PropTypes.func,
    loaded: React.PropTypes.bool,
    userName: React.PropTypes.string,
    data: React.PropTypes.any,
    token: React.PropTypes.string,
};
export default connect(
    mapStateToProps,
    mapDispatchToProps,
)(ProtectedView);
