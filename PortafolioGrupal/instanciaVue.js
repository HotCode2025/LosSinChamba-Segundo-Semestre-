const HolaMundo = {
    data(){
        return {
            mensaje: 'Hola Mundo con Vue.js'
        }
    }
}
Vue.createApp(HolaMundo).mount('#app');
    