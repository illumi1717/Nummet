<template>
    <div class="slae-result">
        <div class="element" v-for="(el, id) in $store.getters['slae/result'].result">
            <span class="element--x">X<sub>{{id + 1}}</sub></span><span style="margin: auto 15px">=</span>{{el}}
        </div>
    </div>
</template>

<script>
    export default {
        name: "slae-result"   
    }
</script>