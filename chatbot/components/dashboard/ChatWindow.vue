<template>
    <v-layout justify-space-between row>
        <v-flex xs12 sm12 md12 lg12 xl12>
            <v-list class="chat-list">
                <template v-for="(message, index) in messages">
                <v-list-tile avatar v-if="message.is_system">
                    <v-list-tile-avatar>
                        <v-img src="/media/img/chatbot.jpg"></v-img>
                    </v-list-tile-avatar>
                    <v-list-tile-content>
                        <v-list-tile-title>
                            <v-chip small class="pa-2" v-text="message.content"></v-chip>
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
                <v-list-tile avatar v-else="!message.is_system">
                    <v-list-tile-content>
                        <v-list-tile-title class="text-xs-right text-sm-right text-md-right text-lg-right text-xl-right">
                            <v-chip small class="pa-2 light-green accent-4" v-text="message.content"></v-chip>
                        </v-list-tile-title>
                    </v-list-tile-content>
                    <v-list-tile-avatar>
                        <v-img src="/media/img/gx.png"></v-img>
                    </v-list-tile-avatar>
                </v-list-tile>
                </template>
            </v-list>
        </v-flex>
    </v-layout>
</template>


<script>

export default {
    name: "ChatWindow",
    props: {
        message: {
            type: "String",
            required: false,
            default: ""
        }
    },
    data () {
        return {
            messages: [
                {
                    content: "Hi, Owen, 你好, 小湘在此等主人很久了。您需要我提供什么样的服务的呢？",
                    is_system: true
                }
            ]
        }
    },
    methods: {
        send: function(){
            console.log('send message = ', this.message);
            this.$http.post("/api/service/", {
                message: this.message
            }).then((response) => {
                this.messages.push(response.data.data.object);
                this.message = "";
            });
        }
    },
    watch: {
        "message": function(newValue, oldValue){
            if(newValue){
                this.messages.push({ content: newValue, is_system: false });
                this.$emit("received");
                this.send();
            }
        }
    }
}

</script>