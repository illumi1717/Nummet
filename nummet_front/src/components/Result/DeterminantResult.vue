<template>
    <div class="determinant-result">
        <span>
            D(A)
            <span style="margin: auto 15px">=</span>
            {{$store.getters['determinant/resultDeterminant']['result']}}
        </span>
    </div>
</template>

<script>
    export default {
        name: "determinant-result"        
    }
</script>
