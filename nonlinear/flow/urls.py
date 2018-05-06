from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('releases', views.releases, name='releases'),
    path('contact', views.contact_form, name='contact'),
    path('', views.index, name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
