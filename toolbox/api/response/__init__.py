from toolbox.api.response.messages import APIMessage, HTTP_200_OK, HTTP_400_BAD_REQUEST

class APIResponse:

    def __init__(self):
        self.object, self.message = None, ""

    @classmethod
    def success_response(cls, data, message=None):
        response = dict(data=data, status=HTTP_200_OK)
        if message:
            response.update(message=APIMessage.success_message(message))
        return response

    @classmethod
    def error_response(cls, errors, message=None):
        response = dict(errors=errors, status=HTTP_400_BAD_REQUEST)
        if message:
            response.update(message=APIMessage.error_message(message))
        return response

    @classmethod
    def make_response(cls, dicts):
        return dicts
