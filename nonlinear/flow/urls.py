from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    # url(r'^blog/', views.blog, name='blog'),
    # url(r'^releases', views.releases, name='releases'),
    # url(r'^contact/', views.contact_form, name='contact'),
    url(r'', views.index, name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]