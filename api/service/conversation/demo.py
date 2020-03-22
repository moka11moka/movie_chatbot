from chatterbot import ChatBot
from src.Movie_main import conversation
class ServiceChatBot:

    NOT_FOUND = 'Sorry, I do not understand.'

    @classmethod
    def get_item(cls, key):
        chatbot = ChatBot('Leo')

        #response = chatbot.get_response(key)
        response = conversation(key)
        return str(response)


