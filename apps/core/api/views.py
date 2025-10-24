from django.http import JsonResponse


def health_view(request):
    """Simple health check endpoint.

    Returns 200 OK with a minimal JSON payload so that the API "serves something"
    even when no other core endpoints are defined.
    """
    return JsonResponse({
        "status": "ok",
        "service": "core",
    })
