import myVue from './index.js'
import ChatWindow from '../components/dashboard/ChatWindow.vue'


var app = new Vue({
    el: "#app",
    components: {
        chatWindow: ChatWindow,
    },
    data(){
        return {}
    }
});