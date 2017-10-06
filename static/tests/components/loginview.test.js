/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { LoginView } from '../../src/components/LoginView';

describe('Component: Login View', () => {
    const wrapper = shallow(<LoginView />);
    test('render without exploding', () => {
        expect(wrapper.contains(<h2>Login to 7 Wonders</h2>)).toEqual(true);
    });
});
