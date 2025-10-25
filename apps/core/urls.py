from django.urls import path, include
from apps.posts import views as post_views

app_name = 'core'

urlpatterns = [
    # Home redirects to blog list
    path('', post_views.blog, name='home'),

    # Keep blog section functional under core responsibility
    # Legacy blog-like endpoints directly mapping to posts views
    path('search/', post_views.search_posts, name='post_search'),
]
