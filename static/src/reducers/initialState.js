const initialState = {
    game: {
        game: null,
        error: false,
        started: false,
        loading: true,
        players: null,
        cardPlayed: null,
        cardValid: null,
        pollId: null,
        clearInterval: false,
    },
    data: {
        data: null,
        isFetching: false,
        loaded: false,
    },
    auth: {
        token: null,
        userName: null,
        isAuthenticated: false,
        isAuthenticating: false,
        statusText: null,
        isRegistering: false,
        isRegistered: false,
        registerStatusText: null,
    },
};

export default initialState;
