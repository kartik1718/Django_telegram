from django.contrib.auth.backends import ModelBackend

from .models import UserAuth

class PasswordlessAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, **kwargs):
        """
        Returns existing user instance if it exists,
        creates a new user otherwise
        """
        if not(username):
            return None
        try:
            user = UserAuth.objects.get(username=username)
        except UserAuth.DoesNotExist:
            user = UserAuth.objects.create(username=username)
        return user
    
    def get_user(self, username):
        try:
            return UserAuth.objects.get(pk=username)
        except UserAuth.DoesNotExist:
            return None