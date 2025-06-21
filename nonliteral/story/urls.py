# story/urls.py
from django.urls import path
from . import views

app_name = 'story'

urlpatterns = [
    # Authentication
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Story
    path('', views.current_chapter_view, name='current_chapter'),
    path('chapter/', views.current_chapter_view, name='chapter'),
    path('choice/<int:choice_id>/', views.make_choice_view, name='make_choice'),
    path('start/', views.start_adventure_view, name='start_adventure'),
    path('reset/', views.reset_adventure_view, name='reset_adventure'),

    # Profile
    path('profile/', views.profile_view, name='profile'),

    # API
    path('api/stats/', views.get_user_stats, name='api_stats'),
]
