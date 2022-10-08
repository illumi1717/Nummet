<template>
    <div class="circle-slider">
        <slider 
            @change="v => $emit('update:modelValue', v)"
            :modelValue="modelValue"
            orientation="circular"
            color="#21ED47" 
            track-color="#3C3C3C"
            :width="'100px'"
            :height="10"
            :min="2"
            :max="7.0"
            :step="1.0"
        />
        <div class="slider-value">{{modelValue}}</div>
        <div v-if="title" class="slider-title">{{title}}</div>
    </div>
</template>

<script>
    import Slider from 'vue3-slider';
    
    export default {
        name: "circle-slider",

        components: {
            Slider
        },

        props: ["title", "modelValue"]
    }
</script>