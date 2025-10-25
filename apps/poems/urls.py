from django.urls import path
from . import views

app_name = 'poems'

urlpatterns = [
    path('', views.poems, name='poem_list'),
]
