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
    REQUEST_PLAY_CARD,
    ERROR_PLAY_CARD,
    RECEIVE_PLAY_CARD,
    CLEAR_INVALID_CARD_ERROR,
} from '../constants/index';
import { createReducer } from '../utils/misc';

const initialState = {
    game: null,
    error: false,
    started: false,
    loading: true,
    players: null,
    cardPlayed: null,
    cardValid: null,
};

export default createReducer(initialState, {
    [RECEIVE_GAME_STATUS]: (state, payload) =>
        Object.assign({}, state, {
            game: payload.game,
            playerCount: payload.players,
            error: false,
            started: payload.started,
            loading: false,
            cardPlayed: payload.cardPlayed,
            clearInterval: payload.clearInterval,
        }),
    [REQUEST_GAME_STATUS]: state =>
        Object.assign({}, state, {
            loading: true,
            error: false,
        }),
    [ERROR_GAME_STATUS]: state =>
        Object.assign({}, state, {
            error: true,
        }),
    [RECEIVE_START_GAME]: (state, payload) =>
        Object.assign({}, state, {
            game: payload.game,
            error: false,
            started: payload.started,
            loading: false,
            clearInterval: payload.clearInterval,
        }),
    [REQUEST_START_GAME]: state =>
        Object.assign({}, state, {
            loading: true,
            error: false,
        }),
    [ERROR_START_GAME]: state =>
        Object.assign({}, state, {
            error: true,
        }),
    [REQUEST_END_GAME]: state =>
        Object.assign({}, state, {
            loading: true,
        }),
    [RECEIVE_END_GAME]: (state, payload) =>
        Object.assign({}, state, {
            loading: false,
            error: false,
            game: null,
            clearInterval: payload.clearInterval,
        }),
    [ERROR_END_GAME]: state =>
        Object.assign({}, state, {
            error: true,
        }),
    [RECEIVE_PLAY_CARD]: (state, payload) => {
        return {
            ...state,
            error: false,
            loading: false,
            cardValid: payload.cardValid,
        };
    },
    [REQUEST_PLAY_CARD]: state =>
        Object.assign({}, state, {
            loading: true,
        }),
    [ERROR_PLAY_CARD]: state =>
        Object.assign({}, state, {
            loading: false,
            error: true,
            cardValid: false,
        }),
    [CLEAR_INVALID_CARD_ERROR]: (state) => {
        return {
            ...state,
            cardValid: null,
        };
    },
});
