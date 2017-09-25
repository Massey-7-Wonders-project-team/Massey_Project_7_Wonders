/* global describe, test, expect */
import * as game from '../../src/actions/game';
import {
    RECEIVE_GAME_STATUS,
    REQUEST_GAME_STATUS,
    ERROR_GAME_STATUS,
} from '../../src/constants/index';

describe('Actions: Game', () => {
    let dummyData;
    test('receiveProtectedData returns the data plus REQUEST_GAME_STATUS', () => {
        dummyData = {};
        const returnData = game.requestGameStatus();
        const expectedReturnData = {
            type: REQUEST_GAME_STATUS,
        };
        expect(returnData).toEqual(expectedReturnData);
    });
    test('receiveProtectedData returns the data plus RECEIVE_PROTECTED_DATA', () => {
        dummyData = {"data": "Sending Dummy Text"};
        const returnData = game.receiveGameStatus(dummyData);
        const expectedReturnData = {
          type: RECEIVE_GAME_STATUS,
          payload: dummyData,
        };
        expect(returnData).toEqual(expectedReturnData);
    });
    test('receiveProtectedData returns the wrong data plus RECEIVE_PROTECTED_DATA', () => {
        dummyData = {"data": "Sending Dummy Text"};
        const returnData = game.receiveGameStatus(dummyData);
        const expectedReturnData = {
          type: RECEIVE_GAME_STATUS,
          payload: "Fake Data",
        };
        expect(returnData).not.toEqual(expectedReturnData);
    });
    test('receiveProtectedData returns the data plus ERROR_GAME_STATUS', () => {
        const returnData = game.gameStatusFailed();
        const expectedReturnData = {
          type: ERROR_GAME_STATUS,
        };
        expect(returnData).toEqual(expectedReturnData);
    });
    test('receiveProtectedData returns wrong ERROR_GAME_STATUS', () => {
        const returnData = game.gameStatusFailed();
        const expectedReturnData = {
          type: RECEIVE_GAME_STATUS
        };
        expect(returnData).not.toEqual(expectedReturnData);
    });
});
