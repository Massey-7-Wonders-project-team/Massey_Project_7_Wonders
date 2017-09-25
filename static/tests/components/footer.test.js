/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { Footer } from '../../src/components/Footer/index';

describe('<Footer />', () => {
    test('renders <Footer />', () => {
        const wrapper = shallow(<Footer />);
        expect(typeof wrapper.find('© DZT 2016').text()).toEqual('string');
    });
});
