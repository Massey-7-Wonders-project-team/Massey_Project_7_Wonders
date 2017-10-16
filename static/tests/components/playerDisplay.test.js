/* global describe, test, expect */

import React from 'react';
import { shallow } from 'enzyme';

import { PlayerDisplay } from '../../src/components/PlayerDisplay';

describe('Component: Player Display', () => {
    const minProps = {
        error: false,
        started: true,
        id: 1,
        boardData: { wonder_level: 0, userId: 1, points: 1, military: 1, profile: 'a' },
        game: { allPlayers: {
            0: { wonder_level: 1, userId: 1, points: 1, military: 1, profile: 'a', wonder: 'The Temple of Artemis in Ephesus', wood: 0, blue: 0, brick: 0, brown: 0, cloth: 0, glass: 0, paper: 0, cog: 0, ore: 0, stone: 0, compass: 0, extra_ore: 0, extra_brick: 0, extra_cloth: 0, extra_wood: 0, extra_glass: 0, extra_stone: 0, extra_paper: 0, military_loss: 0, tablet: 0, left_id: 2, right_id: 3 },
            1: { wonder_level: 1, userId: 2, points: 1, military: 1, profile: 'b', wonder: 'The Hanging Gardens of Babylon', wood: 0, blue: 0, brick: 0, brown: 0, cloth: 0, glass: 0, paper: 0, cog: 0, ore: 0, stone: 0, compass: 0, extra_ore: 0, extra_brick: 0, extra_cloth: 0, extra_wood: 0, extra_glass: 0, extra_stone: 0, extra_paper: 0, military_loss: 0, tablet: 0, left_id: 1, right_id: 3 },
            2: { wonder_level: 1, userId: 3, points: 1, military: 1, profile: 'c', wonder: 'The Statue of Zeus in Olympia', wood: 0, blue: 0, brick: 0, brown: 0, cloth: 0, glass: 0, paper: 0, cog: 0, ore: 0, stone: 0, compass: 0, extra_ore: 0, extra_brick: 0, extra_cloth: 0, extra_wood: 0, extra_glass: 0, extra_stone: 0, extra_paper: 0, military_loss: 0, tablet: 0, left_id: 2, right_id: 1 },
        },
            game: { age: 1, completed: false, id: 1, round: 1, started: true },
            player: { wonder_level: 1, userId: 1, points: 1, military: 1, profile: 'a', wonder: 'The Temple of Artemis in Ephesus', wood: 0, blue: 0, brick: 0, brown: 0, cloth: 0, glass: 0, paper: 0, cog: 0, ore: 0, stone: 0, compass: 0, extra_ore: 0, extra_brick: 0, extra_cloth: 0, extra_wood: 0, extra_glass: 0, extra_stone: 0, extra_paper: 0, military_loss: 0, tablet: 0, left_id: 2, right_id: 3 },
            history: [[{ card_colour: "wonder", card_name: "ephesus_0", playerId: 1 }]],
            wonder: { id: 1, name: 'a', slots: 0, card_0: 'a' }
        },
    };
    const wrapper = shallow(<PlayerDisplay {...minProps} />);
    test('render without exploding', () => {
        expect(wrapper.find('.PlayerDisplayBoard').exists()).toEqual(true);
    });
});
