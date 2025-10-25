from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about, name='about'),
    # Alias contact route to the same view so {% url 'about:contact' %} resolves
    path('contact/', views.about, name='contact'),
]
