# story/auth_backend.py
from django.contrib.auth.backends import BaseBackend
from .models import ReaderUser


class ReaderUserBackend(BaseBackend):
    """Custom authentication backend for ReaderUser"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = ReaderUser.objects.get(username=username)
            if user.check_password(password) and user.is_active:
                return user
        except ReaderUser.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return ReaderUser.objects.get(pk=user_id)
        except ReaderUser.DoesNotExist:
            return None
