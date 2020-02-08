from rest_framework.authentication import BasicAuthentication


class ExemptAuthenticationPermission(BasicAuthentication):
    """
        Not required to check the authentication
    """
    def authenticate(self, request):
        user = getattr(request._request, 'user', None)

        return (user, None)