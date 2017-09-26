/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { AuthenticatedComponent } from '../../src/components/AuthenticatedComponent';

describe('<AuthenticatedComponent />', () => {
    const minProps = {
        token: 'a',
        userName: 'a',
        isAuthenticated: true,
    };
    test('renders <AuthenticatedComponent />', () => {
        const wrapper = shallow(<AuthenticatedComponent />); // not rendering??
        expect(typeof wrapper.find(<AuthenticatedComponent />).length()).toEqual(1);
    });
});
