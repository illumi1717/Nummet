<template>
    <Transition name="error">
        <div class="error-message" v-if="show">
            {{text}}
        </div>
    </Transition>
</template>

<script>
    export default {
        name: "error-message",
        props: ["show", "text"]
    }
</script>