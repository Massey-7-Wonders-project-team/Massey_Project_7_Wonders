/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { AuthenticatedComponent } from '../../src/components/AuthenticatedComponent';

describe('<AuthenticatedComponent />', () => {
    test('renders <AuthenticatedComponent />', () => {
        const wrapper = shallow(<AuthenticatedComponent />);
        this.state.isAuthenticated = true;
        this.state.loaded_if_needed = true;
        expect(typeof wrapper.find(<AuthenticatedComponent {...this.props} />));
    });
});
