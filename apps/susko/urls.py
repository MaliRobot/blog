from django.urls import path

from . import views

app_name = "susko"

urlpatterns = [
    path("", views.susko, name="susko"),
]
