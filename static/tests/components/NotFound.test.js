/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { NotFound } from '../../src/components/NotFound';

describe('Component: Not Found', () => {
    const wrapper = shallow(<NotFound />);
    test('render without exploding', () => {
        expect(wrapper.contains(<h1>Not Found</h1>)).toEqual(true);
    });
});
