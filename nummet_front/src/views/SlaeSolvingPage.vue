<template>
    <div class="slae-solving-page">
        <div class="header-text">The number of unknown values in the system</div>
        <div class="dimension-menu">
            <circle-slider 
                v-model="dimension" 
            />
            <mini-button 
                @click="generateMatrix"
            >
                Generate
            </mini-button>
        </div>
        <div 
            class="slae--container" 
            v-if="$store.getters['matrix/getMatrixLength']"
        >
            <slae-field/>
            <div class="bottom--menu">
                <mini-button
                    @click="$store.dispatch('slae/sendMatrix')"
                >Solve
                </mini-button>
                <mini-button
                    @click="$router.push('/')"
                >Menu
                </mini-button>
                <error-message :show="$store.getters['slae/isError']" :text="$store.getters['slae/errorText']"/>
            </div>
        </div>
    </div>
</template>

<script>
    import CircleSlider from '@/components/CircleSlider/CircleSlider.vue';
    import MiniButton from '@/components/MiniButton.vue';
    import SlaeField from '@/components/SlaeField/SlaeField.vue';
    import ErrorMessage from '@/components/ErrorMessage.vue';
    import BackButton from '@/components/BackButton.vue';
    import { mapGetters } from 'vuex';

    export default {
        data: () => ({
            dimension: 3
        }),

        methods: {
            generateMatrix() {
                this.$store.commit('matrix/clearData')
                this.$store.commit(
                    'matrix/setDimension', 
                    {
                        ndim: this.dimension + 1, 
                        mdim: this.dimension
                    })
                this.$store.commit('matrix/genMatrix')
            }
        },

        computed: {
            ...mapGetters('slae', ['result'])
        },

        watch: {
            result() {
                this.$router.push(`/result?type=slae`);
            }
        },

        components: {
            CircleSlider,
            MiniButton,
            SlaeField,
            ErrorMessage,
            BackButton
        }
    }
</script>