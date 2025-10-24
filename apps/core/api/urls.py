from django.urls import path
from .views import health_view

# Core API endpoints
urlpatterns = [
    path('health/', health_view, name='api-health'),
]
