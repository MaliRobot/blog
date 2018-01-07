from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blog/', views.blog, name='blog'),
    url(r'^releases', views.releases, name='releases'),
    url(r'^contact/', views.contact_form, name='contact'),
    url(r'', views.index, name='index'),
]