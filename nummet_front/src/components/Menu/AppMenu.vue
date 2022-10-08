<template>
    <div class="menu--container">
        <div class="menu">
            <logo />
            <menu-button @click="$router.push('/slae-solving-page')">Solving the SLAE</menu-button>
            <menu-button @click="$router.push('/matrix-operation')">Matrix operations</menu-button>
        </div>
    </div>
</template>

<script>
    import MenuButton from './MenuButton.vue';
    import Logo from './Logo.vue';

    export default {
        name: "app-menu",
        components: {
            MenuButton,
            Logo
        }
    }
</script>
