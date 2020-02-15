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
                    <v-textarea flat solo clearable auto-grow rows="1" placeholder="Enter message here..." class="ma-0 pa-0 textarea" @keydown="send" v-model="content" v-if="!isSpeech">
                        <template v-slot:prepend>
                            <v-icon color="primary" @click="switchMode">mic</v-icon>
                        </template>
                        <template v-slot:append-outer>
                            <v-icon color="primary" @click="send">send</v-icon>
                        </template>
                    </v-textarea>
                    <template v-if="isSpeech">
                        <v-btn icon @click="switchMode">
                            <v-icon color="primary">keyboard</v-icon>
                        </v-btn>
                        <speech-text @speechcompatibility="canSpeech" @speechend="speechEnd" v-if="isSpeech"></speech-text>
                    </template>
                </v-toolbar>
            </v-flex>
        </v-layout>
        <v-dialog v-model="dialog" persistent max-width="290">
            <v-card>
                <v-card-title class="headline pb-2">Oops!</v-card-title>
                <v-card-text class="pt-2" v-text="speechError"></v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="dialog = false">OK</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>


<script>

import SpeechText from './SpeechText.vue';

export default {
    name: "ChatWindow",
    components: {
        speechText: SpeechText
    },
    data(){
        return {
            content: "",
            speechError: "",
            isSpeech: false,
            dialog: false,
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
            if(e.keyCode === 13 && !e.shiftKey && this.content){
                e.preventDefault();
                this.post(this.content);
            }
        },
        post: function(){
            this.$http.post("/api/service/", {
                content: this.content
            }).then((response) => {
                this.messages.push({"content": this.content, "is_system": false});
                this.messages.push(response.data.data.object);
                this.content = "";
                this.updateListScrollPosition();
            });
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
        },
        switchMode: function(){
            this.isSpeech = !this.isSpeech;
        },
        canSpeech: function(obj){
            this.dialog = true;
            this.speechError = obj.error;
        },
        speechEnd: function(obj){
            if(obj.transcript){
                this.content = obj.transcript;
                this.post();
            }
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

.v-toolbar__content {
    padding: 0 16px !important;
}

</style>