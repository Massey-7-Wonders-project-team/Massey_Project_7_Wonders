/* global describe, test, expect */
import createReducer from '../../src/reducers/auth';
import {
    LOGIN_USER_SUCCESS,
    LOGIN_USER_FAILURE,
    LOGIN_USER_REQUEST,
    LOGOUT_USER,
    REGISTER_USER_FAILURE,
    REGISTER_USER_REQUEST,
    REGISTER_USER_SUCCESS,
} from '../../src/constants/index';

describe('Auth reducer', () => {
  const initialState = {
    token: null,
    userName: null,
    isAuthenticated: false,
    isAuthenticating: false,
    statusText: null,
    isRegistering: false,
    isRegistered: false,
    registerStatusText: null,
  };
  it('should return the initial state', () => {
      const returnedData = createReducer(undefined, {});
      const expectedReturnData = initialState
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('LOGIN_USER_REQUEST should return isAuthenticating=true+statusText=null', () => {
      const returnedData = createReducer(undefined, { type: LOGIN_USER_REQUEST });
      const expectedReturnData = {
        token: null,
        userName: null,
        isAuthenticated: false,
        isAuthenticating: true,
        statusText: null,
        isRegistering: false,
        isRegistered: false,
        registerStatusText: null,
      }
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('LOGIN_USER_FAILURE should return statusText=Auth Error...', () => {
      const returnedData = createReducer(undefined, {
          type: LOGIN_USER_FAILURE,
          payload: {
              status: 'Status example',
              statusText: 'Status Text example'
          }});
      const expectedReturnData = {
        token: null,
        userName: null,
        isAuthenticated: false,
        isAuthenticating: false,
        statusText: null,
        isRegistering: false,
        isRegistered: false,
        registerStatusText: null,
        statusText: `Authentication Error: Status example Status Text example`,
      }
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('REGISTER_USER_FAILURE should return statusText=Register Err...', () => {
      const returnedData = createReducer(undefined, {
          type: REGISTER_USER_FAILURE,
          payload: {
              status: 'Status example2',
              statusText: 'Status Text example2'
          }});
      const expectedReturnData = {
        token: null,
        userName: null,
        isAuthenticated: false,
        isAuthenticating: false,
        statusText: null,
        isRegistering: false,
        isRegistered: false,
        registerStatusText: `Register Error: Status example2 Status Text example2`,
        statusText: null,
      }
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('LOGOUT_USER should return statusText=You have...', () => {
      const returnedData = createReducer(undefined, {type: LOGOUT_USER });
      const expectedReturnData = {
        token: null,
        userName: null,
        isAuthenticated: false,
        isAuthenticating: false,
        statusText: null,
        isRegistering: false,
        isRegistered: false,
        registerStatusText: null,
        statusText: 'You have been successfully logged out.',
      }
      expect(returnedData).toEqual(expectedReturnData);
  });
  it('REGISTER_USER_REQUEST should return isRegistering=true', () => {
      const returnedData = createReducer(undefined, { type: REGISTER_USER_REQUEST });
      const expectedReturnData = {
        token: null,
        userName: null,
        isAuthenticated: false,
        isAuthenticating: false,
        statusText: null,
        isRegistering: true,
        isRegistered: false,
        registerStatusText: null,
      }
      expect(returnedData).toEqual(expectedReturnData);
    });
});
