# story/middleware.py
from django.utils.deprecation import MiddlewareMixin
from .models import ReaderUser


class ReaderAuthMiddleware(MiddlewareMixin):
    """Custom middleware to handle ReaderUser authentication"""

    def process_request(self, request):
        # Check if reader is logged in via session
        reader_id = request.session.get('reader_user_id')
        if reader_id:
            try:
                request.reader = ReaderUser.objects.get(id=reader_id, is_active=True)
            except ReaderUser.DoesNotExist:
                request.reader = None
                if 'reader_user_id' in request.session:
                    del request.session['reader_user_id']
        else:
            request.reader = None
