from django.urls import include, path
from django.views.generic import TemplateView

from apps.posts import views as post_views

from . import views as core_views

app_name = "core"

urlpatterns = [
    path(
        "susko/",
        TemplateView.as_view(template_name="susko.html"),
        name="susko",
    ),
]
