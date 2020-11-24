from .models import AccessLog
from django.conf import settings
from django.utils import timezone


class AccessLogsMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # create session
        if not request.session.session_key:
            request.session.create()

        access_logs_data = dict()
        response = self.get_response(request)

        # exclusions
        if request.path.startswith(settings.MEDIA_URL) or request.path.startswith(settings.STATIC_URL) \
                or request.path.startswith('/admin'):
            return response

        # get the request path
        access_logs_data["path"] = request.path

        # get the client's IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        access_logs_data["ip_address"] = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
        access_logs_data["method"] = request.method
        access_logs_data["referrer"] = request.META.get('HTTP_REFERER',None)
        access_logs_data["session_key"] = request.session.session_key

        data = dict()
        data["get"] = dict(request.GET.copy())
        data['post'] = dict(request.POST.copy())

        # remove password form post data for security reasons
        keys_to_remove = ["password", "csrfmiddlewaretoken"]
        for key in keys_to_remove:
            data["post"].pop(key, None)

        access_logs_data["data"] = data
        access_logs_data["timestamp"] = timezone.now()

        try:
            AccessLog(**access_logs_data).save()
        except Exception as e:
            pass

        return response
