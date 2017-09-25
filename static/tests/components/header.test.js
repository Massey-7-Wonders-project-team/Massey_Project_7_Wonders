/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { Header } from '../../src/components/Header/index';

describe('<Header />', () => {
    test('renders <Header />', () => {
        const wrapper = shallow(<Header />);
        this.state.open = true;
        expect(typeof wrapper.find('Nav-Drawer').text()).toEqual('string');
    });
});
