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
from flow import views as flow_views
from django.conf.urls.static import static
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'news', flow_views.NewsViewSet)
router.register(r'posts', flow_views.PostViewSet)
router.register(r'albums', flow_views.AlbumViewSet)
router.register(r'poems', flow_views.PoemViewSet)
router.register(r'events', flow_views.EventViewSet)

urlpatterns = [
    path('', flow_views.index),
    path('admin/', admin.site.urls),
    path('blog/<int:pk>/', flow_views.single_post),
    path('blog', flow_views.blog),
    path('poetry', flow_views.poems),
    path('releases', flow_views.releases),
    path('events', flow_views.events),
    path('contact', flow_views.contact_form),
    path('about', flow_views.about),
    path('api/', include(router.urls)),
    # path('', flew.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
