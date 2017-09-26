/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { Header } from '../../src/components/Header/index';

describe('<Header />', () => {
    const minProps = {
        open: true,
    };
    test('renders <Header />', () => {
        const wrapper = shallow(<Header {...minProps} />);
        expect(typeof wrapper.find('Nav-Draw').text()).toEqual('string');
    });
});
