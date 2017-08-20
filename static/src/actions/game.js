import {
    RECEIVE_GAME_STATUS,
    REQUEST_GAME_STATUS,
    ERROR_GAME_STATUS,
    REQUEST_START_GAME,
    RECEIVE_START_GAME,
    ERROR_START_GAME,
} from '../constants/index';

export function requestGameStatus() {
    return {
        type: REQUEST_GAME_STATUS,
    };
}

export function receiveGameStatus(payload) {
    console.log(payload)
    return {
        type: RECEIVE_GAME_STATUS,
        payload,
    };
}

export function gameStatusFailed() {
    return {
        type: ERROR_GAME_STATUS,
    };
}

export function checkGameStatus(playerId) {
    return (dispatch) => {
        dispatch(requestGameStatus());
        const token = localStorage.getItem('token');
        fetch(`/api/game/status?player_id=${playerId}`, {
            method: 'get',
            credentials: 'include',
            headers: {
                'Accept': 'application/json', // eslint-disable-line quote-props
                'Content-Type': 'application/json',
                Authorization: token,
            },
        })
        .then(response => response.json())
        .then((body) => {
            console.log(body);
            if (body.status === 'Started') {
                dispatch(receiveGameStatus({ game: body.game, started: true }));
            } else {
                dispatch(receiveGameStatus({ game: body.game, started: false }));
            }
        })
        .catch((err) => {
            // catch error
            console.log(err);
            dispatch(gameStatusFailed({ game: null, started: false, error: true }));
        });
    };
}

function requestStartGame() {
    return {
        type: REQUEST_START_GAME,
    };
}

function receiveStartGame(payload) {
    return {
        type: RECEIVE_START_GAME,
        payload,
    };
}

function errorStartGame() {
    return {
        type: ERROR_START_GAME,
    };
}

export function startGame(playerId) {
    return (dispatch) => {
        dispatch(requestStartGame());
        const token = localStorage.getItem('token');
        fetch(`/api/game/start?player_id=${playerId}`, {
            method: 'get',
            credentials: 'include',
            headers: {
                'Accept': 'application/json', // eslint-disable-line quote-props
                'Content-Type': 'application/json',
                Authorization: token,
            },
        })
        .then(response => response.json())
        .then(response => response.json())
        .then((body) => {
            console.log(body);
            dispatch(receiveStartGame({ game: body.game, started: true, players: body.players }));
        })
        .catch((err) => {
            // catch error
            console.log(err);
            dispatch(errorStartGame({ game: null, started: false, error: true }));
        });
    };
}
