from django.conf import settings
from django.conf.urls import include, url, re_path
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('blog/<int:pk>/', views.single_post, name='single_post'),
    path('blog', views.blog, name='blog'),
    path('releases', views.releases, name='releases'),
    path('contact', views.contact_form, name='contact'),
    path('about', views.about, name='about'),
    path('', views.index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
