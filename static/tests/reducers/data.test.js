/* global describe, test, expect */
import createReducer from '../../src/reducers/data';
import {
    RECEIVE_PROTECTED_DATA,
    FETCH_PROTECTED_DATA_REQUEST
} from '../../src/constants/index';

describe('Data reducer', () => {
  const initialState = {
      data: null,
      isFetching: false,
      loaded: false,
  };
  it('should return the initial state', () => {
      const returnedData = createReducer(undefined, {});
      const expectedReturnData = initialState
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('RECEIVE_PROTECTED_DATA should return payload +loading=true', () => {
      const returnedData = createReducer(undefined, {
          type: RECEIVE_PROTECTED_DATA,
          payload: {
              data: "Simple Data",
          }});
      const expectedReturnData = {
        data: "Simple Data",
        isFetching: false,
        loaded: true,
      }
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('FETCH_PROTECTED_DATA_REQUEST should return isFetching=true', () => {
      const returnedData = createReducer(undefined, { type: FETCH_PROTECTED_DATA_REQUEST });
      const expectedReturnData = {
        data: null,
        isFetching: true,
        loaded: false,
      }
      expect(returnedData).toEqual(expectedReturnData);
  });
});
