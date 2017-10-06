/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';
import FlatButton from 'material-ui';
import { PlayerDisplay } from '../../src/components/PlayerDisplay';

describe('Component: Player Display', () => {
    const minProps = {
        error: false,
        started: true,
        id: 1,
        boardData: { wonder_level: 0, userId: 1, points: 1, military: 1, profile: 'a' },
        game: { allPlayers: { wonder_level: 0, userId: 1, points: 1, military: 1, profile: 'a', wonder: 'a' },
            game: { age: 1, completed: false, id: 1, round: 1, started: true },
            player: { wonder_level: 0, userId: 1, points: 1, military: 1, profile: 'a', id: 1 },
            wonder: { id: 1, name: 'a', slots: 0, card_0: 'a' }
        },
    };
    const wrapper = shallow(<PlayerDisplay {...minProps} />);
    test('render without exploding', () => {
        expect(wrapper.contains(<FlatButton label="Back to your Wonder" onClick={this.lookUser} />)).toEqual(true);
    });
});
