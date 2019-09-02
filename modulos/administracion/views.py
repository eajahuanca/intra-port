from rest_framework.views import APIView as OriginalAPIView
from modulos.administracion.exceptions import PermissionDenied, UserDoesnotAuthenticated


class APIView(OriginalAPIView):
    def permission_denied(self, request, message=None):
        """If request is not permitted, determine what kind of exception to raise."""
        if request.authenticators and not request.successful_authenticator:
            raise UserDoesnotAuthenticated
        raise PermissionDenied(message=message)
