import axios from 'axios'

export default {
    namespaced: true,

    state: {
        result: null,

        isError: false,
        errorText: ''
    },

    getters: {
        errorText(state) {
            return state.errorText;
        },
        
        isError(state) {
            return state.isError;
        },
        
        result(state) {
            return state.result;
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
            state.isResult = true;
            state.result = result;
        }
    },
    
    actions: {
        sendMatrix({rootGetters, commit}) {
            commit('matrix/normalizeMatrix', null, {root: true});
            axios
                .post("http://localhost:5000/slae/solve-slae", {
                    matrix: rootGetters['matrix/mappedMatrix']
                })
                .then(res => {
                    if (res.data["error"]) {
                        commit('setError', res.data.error);
                        setTimeout(() => {commit('removeError')}, 1500);
                    } else {
                        commit('setResult', res.data);
                    }
                });
        }
    }
}