<template>
    <div class="inverse-result">
        <div class="result-header">Inverse matrix</div>
        <div class="matrix">
            <div v-for="(row, rowId) in $store.getters['inverse/resultInverse']" class="matrix-row">
                <matrix-input 
                    v-for="(val, colId) in row" 
                    :value="$store.getters['inverse/resultInverse'][rowId][colId].toString()"
                />
            </div>
        </div>
    </div>
</template>

<script>
    import MatrixInput from '../MatrixInput.vue';
    export default {
        name: "inverse-result",
        components: {
            MatrixInput
        }        
    }
</script>
