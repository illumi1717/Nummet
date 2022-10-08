<template>
    <div>
        <app-menu/>
    </div>
</template>

<script>
    import AppMenu from '@/components/Menu/AppMenu.vue';

    export default {
        components: {
            AppMenu
        },

        mounted() {
            this.$store.commit('matrix/clearData')
        }
    }
</script>