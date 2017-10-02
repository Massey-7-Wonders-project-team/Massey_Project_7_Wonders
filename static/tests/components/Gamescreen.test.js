/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { GameScreen } from '../../src/components/GameScreen';

describe('Component: GameScreen', () => {
    const minProps = {
        game: { allPlayers: { wonder_level: 0, userId: 1, points: 1, military: 1, profile: 'a' },
            game: { age: 1, completed: false, id: 1, round: 1, started: true },
            player: { wonder_level: 0, userId: 1, points: 1, military: 1, profile: 'a' }
        },
        checkGameStatus: () => {},
        startGame: () => {},
        error: false,
        started: true,
        loading: false,
        cardPlayed: false,
        setPollId: () => {},
        cardValid: false,
        clearInvalidCardError: () => {},
    };
    const wrapper = shallow(<GameScreen {...minProps} />);
    test('render without exploding', () => {
        expect(wrapper.contains(<h2>Age 1, Round 1</h2>)).toEqual(true);
    });
});
