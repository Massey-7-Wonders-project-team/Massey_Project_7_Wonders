import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { Paper, RaisedButton } from 'material-ui';
import { browserHistory } from 'react-router';
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
    padding: 50,
    margin: '20px auto',
    maxWidth: 600,
    textAlign: 'center',
    display: 'block',
    overflow: 'hidden',
};

export class ProtectedView extends React.Component {
    componentDidMount() {
        this.fetchData();
    }


    fetchData() {
        const token = this.props.token;
        this.props.fetchProtectedData(token);
    }

    dispatchNewRoute(route) {
        browserHistory.push(route);
        this.setState({
            open: false,
        });
    }

    render() {
        const Name = (this.props.userName).split('@')[0];
        const primary = true;
        return (
            <div>
                {!this.props.loaded
                    ? <h1>Loading data...</h1>
                    :
                    <div className="row">
                        <div className="col-sm-12 col-md-8">
                            <h1>Welcome</h1>
                            <Paper style={style}>
                                <h1>{ Name }!</h1>
                                <h3><i>({this.props.data.data.email})</i></h3>
                            </Paper>
                            <br />
                            <RaisedButton
                                style={{
                                    width: '100%',
                                    maxWidth: 400,
                                    margin: '0 auto 20px auto',
                                    display: 'block',
                                }}
                                primary={primary}
                                label="Play New Game"
                                onTouchTap={() => this.dispatchNewRoute('/play')}
                            />
                        </div>
                        <div className="col-sm-12 col-md-4 text-center">
                            <img width="100%" style={{ maxWidth: '300px' }} alt="statue" src={'dist/images/background/statue.jpg'} />
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
