import axios from "axios"

export default {
    namespaced: true,

    state: () => ({
        result: null
    }),

    getters: {
        resultDeterminant(state) {
            return state.result;
        }
    },

    mutations: {
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
                .post("http://localhost:5000/det/solve-determinant", {
                    matrix: rootGetters['matrix/mappedMatrix']
                })
                .then(res => {
                    commit('setResult', res.data);
                });
        }
    }
}