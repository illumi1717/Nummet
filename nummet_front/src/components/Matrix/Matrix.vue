<template>
    <div class="matrix">
        <div v-for="(row, rowId) in $store.getters['matrix/matrix']" class="matrix-row">
            <matrix-input 
                v-for="(val, colId) in row" 
                :value="$store.getters['matrix/matrix'][rowId][colId]"
                @update="v => $store.commit('matrix/setMatrixField', {rowId, colId, value: v})"
            />
        </div>
    </div>
</template>

<script>
    import MatrixInput from '../MatrixInput.vue';

    export default {
        name: "matrix",
        components: {
            MatrixInput
        }
    }
</script>