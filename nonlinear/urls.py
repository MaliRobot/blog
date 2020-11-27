"""nonlinear URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.urls import path
from core import views as core_views
from news import views as news_views
from about import views as about_views
from albums import views as album_views
from events import views as event_views
from poems import views as poem_views
from posts import views as post_views
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'news', news_views.NewsViewSet)
router.register(r'posts', post_views.PostViewSet)
router.register(r'albums', album_views.AlbumViewSet)
router.register(r'poems', poem_views.PoemViewSet)
router.register(r'events', event_views.EventViewSet)

urlpatterns = [
    path('', core_views.index),
    path('stavka/', admin.site.urls),
    path('blog/<int:pk>/', post_views.single_post),
    path('blog', post_views.blog),
    path('poetry', poem_views.poems),
    # path('releases', album_views.releases),
    path('events/<int:pk>', event_views.event),
    path('events', event_views.events),
    path('about', about_views.about),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.error_404_view'
handler500 = 'core.views.error_505_view'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
