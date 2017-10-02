/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { RegisterView } from '../../src/components/RegisterView';

describe('Component: Results', () => {
    const wrapper = shallow(<RegisterView />);
    test('render without exploding', () => {
        expect(wrapper.contains(<h2>Register to play!</h2>)).toEqual(true);
    });
});
