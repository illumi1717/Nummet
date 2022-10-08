import axios from "axios"

export default {
    namespaced: true,

    state: () => ({
        result: null,
        isError: false,
        errorText: ''
    }),

    getters: {
        resultInverse(state) {
            return state.result;
        },

        isError(state) {
            return state.isError;
        },

        errorText(state) {
            return state.errorText;
        }
    },

    mutations: {
        setError(state, errorText) {
            state.isError = true;
            state.errorText = errorText;
        },
    
        removeError(state) {
            state.isError = false;
        },

        setResult(state, result) {
            state.result = result;
        },

        clearResult(state) {
            state.result = null;
        }
    },

    actions: {
        sendMatrix({rootGetters, commit}) {
            commit('matrix/normalizeMatrix', null, {root: true});
            axios
                .post("http://localhost:5000/inv/solve-inverse", {
                    matrix: rootGetters['matrix/mappedMatrix']
                })
                .then(res => {
                    if (res.data['error']) {
                        commit('setError', res.data['error']);
                        setTimeout(() => {commit('removeError')}, 1500);
                    } else {
                        commit('setResult', res.data['result']);
                    }
                });
        }
    }
}