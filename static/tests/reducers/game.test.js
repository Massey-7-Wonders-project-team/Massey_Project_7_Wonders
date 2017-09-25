/* global describe, test, expect */
import createReducer from '../../src/reducers/game';
import {
    RECEIVE_GAME_STATUS,
    REQUEST_GAME_STATUS,
    ERROR_GAME_STATUS,
    REQUEST_START_GAME,
    RECEIVE_START_GAME,
    ERROR_START_GAME,
    REQUEST_END_GAME,
    RECEIVE_END_GAME,
    ERROR_END_GAME,
} from '../../src/constants/index';

describe('Game reducer', () => {
  const initialState = {
      game: null,
      error: false,
      started: false,
      loading: true,
      players: null,
      cardPlayed: false,
  };
  const fakeData = {
      text: 'FAKE',
  }
  it('should return the initial state', () => {
      const returnedData = createReducer(initialState, {});
      const expectedReturnData = initialState
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('RECEIVE_GAME_STATUS should return initial + payloadData', () => {
      const returnedData = createReducer(initialState, {
          type: RECEIVE_GAME_STATUS,
          payload: {
              game: 'game1',
              players: '1',
              started: true,
              cardPlayed: false,
              clearInterval: false,
          }});
      const expectedReturnData = {
        game: 'game1',
        playerCount: '1',
        error: false,
        started: true,
        loading: false,
        players: null,
        cardPlayed: false,
        clearInterval: false,
      };
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('REQUEST_GAME_STATUS should return initial data + loading=True + error=false', () => {
      const returnedData = createReducer(initialState, { type: REQUEST_GAME_STATUS });
      const expectedReturnData = {
          game: null,
          error: false,
          started: false,
          loading: true,
          players: null,
          cardPlayed: false,
      };
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('should return initial data + Error Status=True', () => {
      const returnedData = createReducer(initialState, { type: ERROR_GAME_STATUS });
      const expectedReturnData = {
          game: null,
          error: true,
          started: false,
          loading: true,
          players: null,
          cardPlayed: false,
      };
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('RECEIVE_START_GAME should return data + started=true + loading=false', () => {
      const returnedData = createReducer(initialState, {
        type: RECEIVE_START_GAME,
        payload: {
          game: "GAME",
          clearInterval: false,
        }});
      const expectedReturnData = {
          game: "GAME",
          error: false,
          started: true,
          loading: false,
          players: null,
          cardPlayed: false,
          clearInterval: false,
      };
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('REQUEST_START_GAME should return error=false + loading=true', () => {
      const returnedData = createReducer(initialState, {
          type: REQUEST_START_GAME,
          });
      const expectedReturnData = {
          game: null,
          error: false,
          started: false,
          loading: true,
          players: null,
          cardPlayed: false,
      };
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('ERROR_START_GAME should return initial + error=true', () => {
      const returnedData = createReducer(initialState, { type: ERROR_START_GAME });
      const expectedReturnData = {
          game: null,
          error: true,
          started: false,
          loading: true,
          players: null,
          cardPlayed: false,
      };
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('REQUEST_END_GAME should return initial + loading=true', () => {
      const returnedData = createReducer(initialState, { type: REQUEST_END_GAME });
      const expectedReturnData = {
          game: null,
          error: false,
          started: false,
          loading: true,
          players: null,
          cardPlayed: false,
      };
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('RECEIVE_END_GAME should return initial + loading=true', () => {
      const returnedData = createReducer(initialState, {
          type: RECEIVE_END_GAME,
          payload: {
            clearInterval: true,
          }});
      const expectedReturnData = {
          game: null,
          error: false,
          started: false,
          loading: false,
          players: null,
          cardPlayed: false,
          clearInterval: true,
      };
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('ERROR_END_GAME should return initial + error=true', () => {
      const returnedData = createReducer(initialState, { type: ERROR_END_GAME });
      const expectedReturnData = {
        game: null,
        error: true,
        started: false,
        loading: true,
        players: null,
        cardPlayed: false,
      };
      expect(returnedData).toEqual(expectedReturnData);
  });

});
