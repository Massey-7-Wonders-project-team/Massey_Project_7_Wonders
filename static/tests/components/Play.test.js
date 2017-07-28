/* global describe, test, expect */

import React from 'react';
import { mount } from 'enzyme';

import { Play } from '../../src/components/Play';

describe('<Play />', () => {
    test('renders <Play />', () => {
        const wrapper = mount(<Play />);
        expect(typeof wrapper.find('.Game').text()).toEqual('string');
    });
});
