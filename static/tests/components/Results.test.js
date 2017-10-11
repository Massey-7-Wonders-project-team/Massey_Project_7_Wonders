/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { Results } from '../../src/components/Results';

describe('Component: Results', () => {
    const wrapper = shallow(<Results />);
    test('render without exploding', () => {
        expect(wrapper.contains(<h1>Results</h1>)).toEqual(true);
    });
});
