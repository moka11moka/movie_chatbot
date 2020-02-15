<template>
    <v-container fluid class="pa-0" id="container">
        <v-layout align-space-around justify-space-between column fill-height>
            <v-flex xs12 sm12 md12 lg12 xl12>
                <v-list :style="style()" id="list" class="chat-list scroll-y">
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
                <v-toolbar color="light-grey" class="pa-0 pt-1">
                    <v-textarea flat solo clearable auto-grow rows="1" placeholder="Enter message here..." class="ma-0 pa-0 textarea" @keydown="send" v-model="content">
                        <template v-slot:append-outer>
                            <v-icon color="primary" @click="send">send</v-icon>
                        </template>
                    </v-textarea>
                </v-toolbar>
            </v-flex>
        </v-layout>
    </v-container>
</template>


<script>

export default {
    name: "ChatWindow",
    data () {
        return {
            content: "",
            container: null,
            elem: null,
            messages: [
                {
                    content: "Hi, Owen, What can I do for you？",
                    is_system: true
                }
            ]
        }
    },
    methods: {
        send: function(e){
            if(e.keyCode === 13 && !e.shiftKey){
                e.preventDefault();
                this.$http.post("/api/service/", {
                    content: this.content
                }).then((response) => {
                    this.messages.push({"content": this.content, "is_system": false});
                    this.messages.push(response.data.data.object);
                    this.content = "";
                    this.updateListScrollPosition();
                });
            }
        },
        style: function(){
            return {
                maxHeight: (window.innerHeight - 64) + "px",
                height: (window.innerHeight - 128) + "px"
            };
        },
        updateListScrollPosition(){
            setTimeout(() => {
                var list = document.getElementById("list");
                list.scrollTop = list.scrollHeight;
            }, 200);
        }
    }
}

</script>

<style>

.v-textarea.v-text-field--enclosed.v-text-field--single-line textarea {
    margin-top: 0px !important;
}

.textarea .v-input__slot {
    margin-bottom: 0px !important;
}

</style>