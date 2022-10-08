<template>
    <div class="slae-field">
        <div 
            class="slae-row"
            v-for="m in $store.getters['matrix/getDimension'].m" 
        >
            <div v-for="n in ($store.getters['matrix/getDimension'].n - 1)" class="element--container">
                <div class="element"> 
                    <matrix-input 
                        :value="$store.getters['matrix/matrix'][m - 1][n - 1]"
                        @update="v => $store.commit('matrix/setMatrixField', {rowId: m - 1, colId: n - 1, value: v})"
                    />
                    <span class="element--x">X</span><sub>{{n}}</sub>
                </div>
                <div class="sign">
                    <span v-if="n != $store.getters['matrix/getDimension'].m" class="plus">+</span>
                    <span v-else class="plus">=</span>
                </div>
            </div>
            <div class="result">
                <matrix-input 
                    :value="$store.getters['matrix/matrix'][m - 1][$store.getters['matrix/getDimension'].n - 1]"
                    @update="v => $store.commit('matrix/setMatrixField', {rowId: m - 1, colId: $store.getters['matrix/getDimension'].n - 1, value: v})"
                />
            </div>
        </div>
    </div>
</template>

<script>
    import MatrixInput from '../MatrixInput.vue';

    export default {
        name: "slae-field",
        
        components: {
            MatrixInput
        }
    }
</script>