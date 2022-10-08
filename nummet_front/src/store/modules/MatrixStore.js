export default {
    namespaced: true,

    state: () => ({
        dimension: {
            'n': 0,
            'm': 0
        },
        matrix: [],
        mappedMatrix: []
    }),
    
    getters: {
        matrix(state) {
            return state.matrix;
        },
        
        mappedMatrix(state) {
            return state.mappedMatrix;
        },

        getMatrixLength(state) {
            return state.matrix?.length;
        },

        getDimension(state) {
            return state.dimension
        }
    },

    mutations: {
        setDimension(state, ctx) {
            state.dimension.n = ctx.ndim;
            state.dimension.m = ctx.mdim;
        },

        genMatrix(state) {            
            for(let i = 0; i < state.dimension.m; i++) {
                state.matrix.push(Array(state.dimension.n).fill(''));
            }
        },

        setMatrixField(state, params) {
            state.matrix[params.rowId][params.colId] = params.value.replace(/[^\d|\-|\.]/g, '');
        },

        setMatrix(state, matrix) {
            state.matrix = matrix.map(row => row.map(val => val.toString()));
        },

        clearData(state) {
            state.dimension.n = 0;
            state.dimension.m = 0;
            state.matrix = [];
        },

        normalizeMatrix(state) {
            const filteredMatrix = state.matrix.map(row => row.map(val => {
                if (val == '') {
                    return '0';
                } else {
                    return val;
                }
            }));
            const mappedMatrix = filteredMatrix.map(row => row.map(val => parseFloat(val)));
            state.mappedMatrix = mappedMatrix
        }
    }
}