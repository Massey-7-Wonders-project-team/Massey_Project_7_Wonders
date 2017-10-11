/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { ProtectedView } from '../../src/components/ProtectedView';

describe('Component: ProtectedView', () => {
    const minProps = {
        userName: 'h@llo'
    }
    const wrapper = shallow(<ProtectedView {...minProps} />);
    test('render without exploding', () => {
        expect(wrapper.contains(<h1>Loading data...</h1>)).toEqual(true);
    });
});
