<template>
    <div class="result-page">
        <preloader v-if="showPreloader"/>
        <div 
            v-if="!showPreloader"
            class="result-data"
        >
            <div class="result-header">result</div>
            
            <slae-result v-if="$route.query.type == 'slae'"/>
            <determinant-result v-if="$route.query.type == 'matrix'"/>
            <inverse-result v-if="$route.query.type == 'matrix' && $store.getters['inverse/resultInverse']"/>
            
            <mini-button @click="$router.push('/')">Menu</mini-button>
            <mini-button @click="returnSolvePage">Back</mini-button>
        </div>
    </div>
</template>

<script>
    import Preloader from '@/components/Preloader/Preloader.vue';
    import SlaeResult from '@/components/Result/SlaeResult.vue';
    import DeterminantResult from '@/components/Result/DeterminantResult.vue';
    import InverseResult from '@/components/Result/InverseResult.vue';
    import MiniButton from '@/components/MiniButton.vue';

    export default {
        components: {
            Preloader,
            SlaeResult,
            MiniButton,
            DeterminantResult,
            InverseResult
        },

        data: () => ({
            showPreloader: true
        }),

        methods: {
            returnSolvePage() {
                if (this.$route.query.type == "matrix") {
                    this.$router.push("/matrix-operation")
                } else if (this.$route.query.type == "slae") {
                    this.$router.push('/slae-solving-page')
                }
            }
        },

        mounted() {
            setTimeout(() => {
                this.showPreloader = false;
            }, 3000);
        },

        beforeUnmount() {
            this.$store.commit('determinant/clearResult');
            this.$store.commit('inverse/clearResult');
        }
    }
</script>
