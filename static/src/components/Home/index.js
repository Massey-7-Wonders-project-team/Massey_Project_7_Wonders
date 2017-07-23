import React from 'react';
import { browserHistory } from 'react-router';
import { RaisedButton } from 'material-ui';

export class Home extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            open: false,
        };
        this.dispatchNewRoute = this.dispatchNewRoute.bind(this);
    }

    dispatchNewRoute(event, route) {
        event.preventDefault();
        browserHistory.push(route);
        this.setState({
            open: true,
        });
    }

    render() {
        return (
            <section>
                <div className="container text-center">
                    <h1>Welcome</h1>
                    <p>Sign in or Register to begin</p>
                    <RaisedButton
                        label="Sign in"
                        onClick={(e) => this.dispatchNewRoute(e, '/login')}
                        style={{
                            marginRight: '10px',
                        }}
                    />
                    <RaisedButton
                        label="Register"
                        onClick={(e) => this.dispatchNewRoute(e, '/register')}
                        style={{
                            marginLeft: '10px',
                        }}
                    />
                </div>
            </section>
        );
    }
}
