from django.conf import settings
from django.conf.urls import include, url, re_path
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
