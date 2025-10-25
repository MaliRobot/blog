from django.urls import path
from apps.posts import views as post_views

app_name = 'blog'

urlpatterns = [
    # Blog list and details now handled by core, using posts views
    path('', post_views.blog, name='post_list'),
    path('<int:pk>/', post_views.single_post, name='post_detail'),
]
