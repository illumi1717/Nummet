<template>
    <div class="matrix-page">
        <div class="header-text">Dimension of the matrix</div>
        <div class="dimension-menu">
            <div class="sliders">
                <circle-slider 
                    v-model="ndim"
                    :title="'n'"
                />
                <circle-slider 
                    v-model="mdim"
                    :title="'m'"
                />
            </div>
            <mini-button 
                @click="genMatrix"
            >
                Generate
            </mini-button>
        </div>

        <div class="matrix-container">
            <matrix/>
        </div>

        <div class="bottom--menu" v-if="$store.getters['matrix/matrix'].length">
            <div class="matrix-operations">
                <mini-button
                    @click="sendMatrix"
                >Solve
                </mini-button>
                <mini-button
                    @click="autocompleteMatrix"
                >Autocomplete
                </mini-button>
            </div>
            <mini-button
                @click="$router.push('/')"
            >Menu
            </mini-button>
        </div>

        <error-message :show="isError" :text="'The number of rows is not equal to the number of columns'"/>
    </div>
</template>

<script>
    import CircleSlider from '@/components/CircleSlider/CircleSlider.vue';
    import MiniButton from '@/components/MiniButton.vue';
    import Matrix from '@/components/Matrix/Matrix.vue';
    import ErrorMessage from '@/components/ErrorMessage.vue';

    import MatrixAutocomplete from "./service/MatrixAutocomplete";
    import { mapGetters } from 'vuex';

    export default {
        data: () => ({
            ndim: 3,
            mdim: 3,
            isError: false
        }),

        methods: {
            sendMatrix() {
                this.$store.dispatch('determinant/sendMatrix');
                this.$store.dispatch('inverse/sendMatrix');
            },

            genMatrix() {
                if (this.ndim == this.mdim) {
                    this.$store.commit('matrix/clearData');
                    this.$store.commit(
                        'matrix/setDimension', 
                        {
                            ndim: this.ndim, 
                            mdim: this.mdim
                        });
                    this.$store.commit('matrix/genMatrix');
                } else {
                    this.isError = true;
                    setTimeout(() => {
                        this.isError = false;
                    }, 1500);
                }
            }, 

            autocompleteMatrix() {
                const matrix = MatrixAutocomplete.gilbert(this.$store.getters['matrix/getDimension'].n);
                this.$store.commit("matrix/setMatrix", matrix);
            }
        },

        computed: {
            ...mapGetters('determinant', ['resultDeterminant'])
        },

        watch: {
            resultDeterminant() {
                this.$router.push(`/result?type=matrix`);
            }
        },

        components: {
            CircleSlider,
            MiniButton,
            Matrix,
            ErrorMessage
        }
    }
</script>
