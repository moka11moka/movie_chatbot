from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

class serviceChatBot:

    NOT_FOUND = 'Sorry, I do not understand.'

    @classmethod
    def get_item(cls, key):
        chatbot = ChatBot('ran')

        conversation = [
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome."
        ]

        # trainer = ListTrainer(chatbot)
        # trainer.train(conversation)
        response = chatbot.get_response(key)
        return dict(response)


