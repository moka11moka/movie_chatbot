import myVue from './index.js'
import ChatbotPanel from '../components/dashboard/ChatbotPanel.vue'
import ChatContactList from '../components/dashboard/ChatContactList.vue'
import ChatWindow from '../components/dashboard/ChatWindow.vue'


var app = new Vue({
    el: "#app",
    components: {
        chatbotPanel: ChatbotPanel,
        chatContactList: ChatContactList,
        chatWindow: ChatWindow,
    },
    data(){
        return {
            message: ""
        }
    },
    computed: {
        chatWindow() {
            return this.$refs.chatWindow;
        }
    },
    methods: {
        receivedMessage: function(){
            this.message = "";
        },
        sendMessage: function(){
            this.chatWindow.message = this.message;
        }
    }
});