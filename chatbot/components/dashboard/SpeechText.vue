<template>
    <v-btn block :color="!isSpeaking?'white black--text':(isSpeaking?'red white--text':'red darken-3 white--text')" :class="{'animated infinite pulse': isSpeaking}" @click.stop="isSpeaking?stopSpeech():startSpeech()">
        <v-icon>{{isSpeaking?'mic_off':'mic'}}</v-icon>
    </v-btn>
</template>


<script>

export default {
    name: "SpeechText",
    props: {
        lang: {
            type: String,
            default: "en-US"
        },
        errorMessage: {
            type: String,
            default: "Speech Recognition is not available on this browser. Please use Chrome or Firefox"
        }
    },
    data() {
        return {
            isSpeaking: false,
            speaking: false,
            dialog: false,
            transcript: ""
        }
    },
    computed: {
        speechRecognition() {
            return window.SpeechRecognition || window.webkitSpeechRecognition;
        },
        recognition() {
            return this.speechRecognition?new this.speechRecognition():false;
        }
    },
    mounted: function(){
        this.checkSpeechCompatibility();
    },
    methods: {
        checkSpeechCompatibility(){
            if(!this.recognition){
                this.$emit('speechcompatibility', {
                    error: this.errorMessage
                })
                return false;
            }
        },
        startSpeech: function(){
            this.checkSpeechCompatibility();
            this.isSpeaking = true;
            this.recognition.lang = this.lang;
            this.recognition.interimResults = true;

            this.recognition.addEventListener('speechstart', event => {
                this.speaking = true;
            });

            this.recognition.addEventListener('speechend', event => {
                this.speaking = false;
            });

            this.recognition.addEventListener('result', event => {
                var transcript = Array.from(event.results).map(result => result[0]).map(result => result.transcript).join('');
                this.transcript = transcript;
            });

            this.recognition.start();
        },
        stopSpeech: function(){
            this.recognition.stop();
            this.isSpeaking = false;
            this.$emit('speechend', {
                transcript: this.transcript
            });
        }
    }
}

</script>

<style scoped>

.animated {
    animation: pulse 2s infinite;
}

@keyframes pulse {
	0% {
		transform: scale(0.99);
		box-shadow: 0 0 0 0 rgba(0, 0, 0, 0.7);
	}

	70% {
		transform: scale(1);
		box-shadow: 0 0 0 5px rgba(0, 0, 0, 0);
	}

	100% {
		transform: scale(0.99);
		box-shadow: 0 0 0 0 rgba(0, 0, 0, 0);
	}
}

</style>