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
} from '../constants/index';
import { createReducer } from '../utils/misc';

const initialState = {
    game: null,
    error: false,
    started: false,
    loading: true,
    players: null,
    cardPlayed: false,
    completed: false,
};

export default createReducer(initialState, {
    [RECEIVE_GAME_STATUS]: (state, payload) =>
        Object.assign({}, state, {
            game: payload.game,
            playerCount: payload.players,
            error: false,
            started: payload.started,
            completed: payload.completed,
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
            started: true,
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
            completed: payload.completed,
            started: false,
        }),
    [ERROR_END_GAME]: state =>
        Object.assign({}, state, {
            error: true,
        }),
});
