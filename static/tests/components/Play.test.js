/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { Play } from '../../src/components/Play';

describe('<Play />', () => {
    test('renders <Play />', () => {
        const wrapper = shallow(<Play />);
        expect(wrapper.find('.Game').exists()).toEqual(true);
    });
});
