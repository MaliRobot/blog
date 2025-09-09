from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail_slug'),
    path('category/<slug:slug>/', views.CategoryPostListView.as_view(), name='category_posts'),
    path('tag/<slug:slug>/', views.TagPostListView.as_view(), name='tag_posts'),
    path('author/<int:pk>/', views.AuthorPostListView.as_view(), name='author_posts'),
    path('archive/<int:year>/<int:month>/', views.ArchivePostListView.as_view(), name='archive_posts'),
]
