from rest_framework.status import *
from rest_framework.exceptions import *
from rest_framework.views import exception_handler
from django.utils.translation import ugettext_lazy as _
from toolbox.api.constants import message


def api_exception_handler(exc, context):

    response, data, raw = exception_handler(exc, context), None, True

    if isinstance(exc, MethodNotAllowed):
        data = dict(message=message.METHOD_NOT_ALLOWED, status=HTTP_405_METHOD_NOT_ALLOWED)
    elif isinstance(exc, NotAuthenticated) or isinstance(exc, AuthenticationFailed):
        data = dict(message=message.AUTHENTICATE_INVALID, status=HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    elif isinstance(exc, AuthenticationLoginFailed):
        data = dict(message=message.USER_NOT_LOGIN, status=HTTP_400_BAD_REQUEST)
    elif isinstance(exc, AuthenticationLoggedInFailed):
        data = dict(message=message.USER_LOGGED_IN, status=HTTP_400_BAD_REQUEST)
    elif isinstance(exc, NotPermission):
        data = dict(message=message.NOT_PERMISSION, status=HTTP_400_BAD_REQUEST)
    elif isinstance(exc, NotPermissionList):
        data = dict(message=message.NOT_PERMISSION_LIST, status=HTTP_400_BAD_REQUEST)
    elif isinstance(exc, NotPermissionCreate):
        data = dict(message=message.NOT_PERMISSION_ADD, status=HTTP_400_BAD_REQUEST)
    elif isinstance(exc, NotPermissionUpdate):
        data = dict(message=message.NOT_PERMISSION_EDIT, status=HTTP_400_BAD_REQUEST)
    elif isinstance(exc, NotPermissionDelete):
        data = dict(message=message.NOT_PERMISSION_DELETE, status=HTTP_400_BAD_REQUEST)
    elif isinstance(exc, NotPermissionDetails):
        data = dict(message=message.NOT_PERMISSION_DETAILS, status=HTTP_400_BAD_REQUEST)
    elif isinstance(exc, NotPermissionChangePassword):
        data = dict(message=message.NOT_PERMISSION_CHANGE_PASSWORD, status=HTTP_400_BAD_REQUEST)
    elif isinstance(exc, ExpiredAuthenticationToken):
        data = dict(message=message.AUTHENTICATE_TOKEN_EXPIRY, status=HTTP_400_BAD_REQUEST)
    elif isinstance(exc, InvalidTokenException):
        data = dict(message=message.AUTHENTICATE_TOKEN_INVALID, status=HTTP_400_BAD_REQUEST)
    elif isinstance(exc, NotObjectFoundException):
        data = dict(message=message.NOT_OBJECT_FOUND, status=HTTP_400_BAD_REQUEST)
    elif isinstance(exc, AttributeError):
        data = dict(messages=message.NOT_VALID, status=HTTP_400_BAD_REQUEST)

    data['data'] = dict()
    response.data = data

    return response


class AuthenticationLoginFailed(APIException):
    status_code = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
    default_detail = _('')


class AuthenticationLoggedInFailed(APIException):
    status_code = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
    default_detail = _('')


class NotPermission(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('')


class NotPermissionList(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('')


class NotPermissionCreate(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('')


class NotPermissionUpdate(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('')


class NotPermissionDelete(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('')


class NotPermissionDetails(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('')


class ExpiredAuthenticationToken(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('')


class NotPermissionChangePassword(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('')


class NotPermissionAccess(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('')


class InvalidTokenException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('')


class NotObjectFoundException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('')