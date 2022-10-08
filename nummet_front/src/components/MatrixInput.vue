<template>
    <input
        type="number"
        step="0.01"
        
        :value="value"
        @input="v => $emit('update', v.target.value)"

        class="matrix-input"

        :class="{
            'empty': value.length == 0,
            'full': value.length > 0
        }"
    >
</template>

<script>
    export default {
        name: "matrix-input",

        props: ["value"]
    }
</script>
