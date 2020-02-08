from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions
from toolbox.api.exceptions.exceptions import *
# from toolbox.utilities.encodes import base64_encode
# from toolbox.utilities.datetime import stringify_date, today
# from auths.models import User


class ExemptCheckPermission(permissions.BasePermission):
    """
        Not required to check the permission
    """
    def has_permission(self, request, view):
        return True


# class IsLoggedInPermission(permissions.BasePermission):
#     """
#         Check whether a user has logged in
#         If logged in, then the user has a permission to do
#         If not, reject the request
#     """
#
#     def has_permission(self, request, view):
#         if not isinstance(request.user, User):
#             raise AuthenticationLoginFailed()
#         return True
#
#
# class IsTokenExistPermission(permissions.BasePermission):
#     """
#         Check whether a user has logged in
#         If logged in, then the user has a permission to do
#         If not, reject the request
#     """
#
#     def has_permission(self, request, view):
#
#         authorization = request.META.get('HTTP_AUTHORIZATION', None)
#
#         if authorization is None or not authorization:
#             raise NotAuthenticated()
#
#         if 'Token' not in authorization:
#             raise NotAuthenticated()
#
#         token = authorization.replace("Token ", "").strip()
#         user = User.objects.get_one_by_token(token)
#         if not isinstance(user, User):
#             raise NotAuthenticated()
#
#         if user.is_expired():
#             raise ExpiredAuthenticationToken()
#
#         return True
#
#
# class HasTokenPermission(permissions.BasePermission):
#     """
#         Check whether a user has a token
#     """
#
#     def has_permission(self, request, view):
#
#         authorization = request.META.get('HTTP_AUTHORIZATION', None)
#
#         if authorization is None or not authorization:
#             raise NotAuthenticated()
#
#         token = authorization.replace("Token ", "").strip()
#         if not User.objects.token_exist(token):
#             raise NotAuthenticated()
#
#         return True
#
#
# class BaseActionPermission(permissions.BasePermission):
#
#     model, permission, raise_exception = None, None, None
#
#     def has_permission(self, request, view):
#
#         if isinstance(request.user, AnonymousUser):
#             return False
#
#         if not request.user.has_perm(self.permission):
#             raise self.raise_exception()
#
#         return True
#
#
# class BaseViewPermission(BaseActionPermission):
#     """
#         Check whether the user has view permission
#     """
#     model, raise_exception = None, NotPermissionList
#
#
# class BaseListPermission(BaseActionPermission):
#     """
#         Check whether the user has list permission
#     """
#     model, raise_exception = None, NotPermissionList
#
#
# class BaseCreatePermission(BaseActionPermission):
#
#     model, raise_exception = None, NotPermissionCreate
#
#
# class BaseUpdatePermission(BaseActionPermission):
#
#     model, raise_exception = None, NotPermissionUpdate
#
#
# class BaseDeletePermission(BaseActionPermission):
#
#     model, raise_exception = None, NotPermissionDelete
#
#
# class BaseDetailsPermission(BaseActionPermission):
#
#     model, raise_exception = None, NotPermissionDetails
#



