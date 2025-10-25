from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.events, name='event_list'),
    path('<int:pk>/', views.event, name='event_detail'),
]
