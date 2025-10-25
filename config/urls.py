"""
Main URL Configuration for the blog project.

This file routes URLs to the appropriate views and includes app-specific URLs.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.posts import views as post_views

# API URLs
api_patterns = [
    path('v1/', include('apps.core.api.urls')),
    path('v1/blog/', include('apps.core.api.blog_urls')),
    path('v1/news/', include('apps.news.api.urls')),
    path('v1/events/', include('apps.events.api.urls')),
    path('v1/albums/', include('apps.albums.api.urls')),
    path('v1/poems/', include('apps.poems.api.urls')),
]

urlpatterns = [
    # Admin (custom path)
    path('stavka/', admin.site.urls),

    # Root and app routes
    path('', post_views.blog, name='home'),  # explicit home URL name at project root
    path('search/', post_views.search_posts, name='post_search'),
    path('blog/', include('apps.core.blog_urls')),
    path('stories/', include('apps.story.urls')),
    path('news/', include('apps.news.urls')),  # register news namespace
    path('events/', include('apps.events.urls')),
    path('poems/', include('apps.poems.urls')),
    path('about/', include('apps.about.urls')),

    # API
    path('api/', include(api_patterns)),

    # Third-party apps
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    # Debug toolbar
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

# Custom error handlers
handler404 = 'apps.core.views.error_404'
handler500 = 'apps.core.views.error_500'
handler403 = 'apps.core.views.error_403'
handler400 = 'apps.core.views.error_400'
