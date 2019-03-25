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
from flow import views as flew
from django.conf.urls.static import static

urlpatterns = [
    path('', flew.index),
    path('admin/', admin.site.urls),
    path('blog/<int:pk>/', flew.single_post),
    path('blog', flew.blog),
    path('poetry', flew.poems),
    path('releases', flew.releases),
    path('contact', flew.contact_form),
    path('about', flew.about_page),
    # path('', flew.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
