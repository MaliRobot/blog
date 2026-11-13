from unittest.mock import Mock, patch

from django.http import HttpResponse
from django.test import RequestFactory, SimpleTestCase

from .logging_middleware import AccessLogsMiddleware


class AccessLogsMiddlewareTests(SimpleTestCase):
    @patch("apps.access_log.logging_middleware.AccessLog")
    def test_password_fields_are_not_logged(self, access_log):
        request = RequestFactory().post(
            "/signup/",
            {
                "username": "alice",
                "password": "secret",
                "password1": "secret",
                "password2": "secret",
                "PASSWORD_CONFIRM": "secret",
                "csrfmiddlewaretoken": "token",
            },
        )
        request.session = Mock(session_key="session-key")
        middleware = AccessLogsMiddleware(lambda req: HttpResponse())

        middleware(request)

        logged_data = access_log.call_args.kwargs["data"]
        self.assertEqual(logged_data["post"], {"username": ["alice"]})
