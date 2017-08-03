/* global describe, test, expect */
import * as data from '../../src/actions/data';
import { FETCH_PROTECTED_DATA_REQUEST, RECEIVE_PROTECTED_DATA } from '../../src/constants/index';

describe('Actions: Data', () => {
    let dummyData;
    test('receiveProtectedData returns the data plus RECEIVE_PROTECTED_DATA', () => {
        dummyData = {};
        const returnData = data.receiveProtectedData(dummyData);
        const expectedReturnData = {
            payload: {
                data: dummyData,
            },
            type: RECEIVE_PROTECTED_DATA,
        };
        expect(returnData).toEqual(expectedReturnData);
    });
    test('receiveProtectedData returns the data plus RECEIVE_PROTECTED_DATA', () => {
        dummyData = {};
        const returnData = data.receiveProtectedData(dummyData);
        const expectedReturnData = {
            payload: {
                data: dummyData,
            },
            type: RECEIVE_PROTECTED_DATA,
        };
        expect(returnData).toEqual(expectedReturnData);
    });
    test('receiveProtectedData should not return the initial data', () => {
        dummyData = {};
        const returnData = data.receiveProtectedData(dummyData);
        const expectedReturnData = {
            payload: {
                data: 'Fake data',
            },
            type: RECEIVE_PROTECTED_DATA,
        };
        expect(returnData).not.toEqual(expectedReturnData);
    });
    test('fetchProtectedDataRequest returns FETCH_PROTECTED_DATA_REQUEST', () => {
        const returnData = data.fetchProtectedDataRequest();
        expect(returnData).toEqual({
            type: FETCH_PROTECTED_DATA_REQUEST,
        });
    });
});
