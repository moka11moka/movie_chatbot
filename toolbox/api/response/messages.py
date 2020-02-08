from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class APIMessage:

    def __init__(self, text, status):
        self.text, self.status = text, status

    def __dict__(self):
        return dict(text=self.text, color=self.get_color())

    def get_color(self):
        if self.status == HTTP_200_OK:
            return "success"
        elif self.status == HTTP_400_BAD_REQUEST:
            return "error"
        return "info"
    
    @classmethod
    def success_message(cls, text):
        return dict(text=text, color="green")
    
    @classmethod
    def error_message(cls, text):
        return dict(text=text, color="error")
    
    @classmethod
    def info_message(cls, text):
        return dict(text=text, color="info")

