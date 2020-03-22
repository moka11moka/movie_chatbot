# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer
import src.Movie_main
from MYSQL import MYSQL


mysql = MYSQL()


class ServiceChatBot:

    NOT_FOUND = 'Sorry, I do not understand.'

    @classmethod
    def get_item(cls, key):
        # chatbot = src.Movie_main.main(key)

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
        response = src.Movie_main.main(key,mysql)
        return str(response)


