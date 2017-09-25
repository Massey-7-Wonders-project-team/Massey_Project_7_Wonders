/* global describe, test, expect */
import * as login from '../../src/actions/auth';
import {
    LOGIN_USER_REQUEST,
    REGISTER_USER_REQUEST,
} from '../../src/constants/index';


describe('Actions: Login', () => {
    test('registerUserRequest returns REGISTER_USER_REQUEST', () => {
        const returnData = login.registerUserRequest();
        const expectedReturnData = {
              type: REGISTER_USER_REQUEST,
        };
        expect(returnData).toEqual(expectedReturnData);
    });
    test('loginUserRequest returns LOGIN_USER_REQUEST', () => {
        const returnData = login.loginUserRequest();
        const expectedReturnData = {
              type: LOGIN_USER_REQUEST,
        };
        expect(returnData).toEqual(expectedReturnData);
    });

});
