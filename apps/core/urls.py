from django.urls import path, include
from django.views.generic import TemplateView

from . import views as core_views
from apps.posts import views as post_views

app_name = 'core'

urlpatterns = [
    path(
        "susko/",
        TemplateView.as_view(template_name="susko.html"),
        name="susko",
    ),
]
