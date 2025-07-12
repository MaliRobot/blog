# story/urls.py
from django.urls import path
from . import views

app_name = 'story'

urlpatterns = [
    # Home and authentication
    path('', views.home, name='home'),
    path('reader/login/', views.ReaderLoginView.as_view(), name='reader_login'),
    path('reader/logout/', views.ReaderLogoutView.as_view(), name='reader_logout'),
    path('reader/signup/', views.ReaderSignUpView.as_view(), name='reader_signup'),

    # Game functionality
    path('dashboard/', views.dashboard, name='dashboard'),
    path('chapter/', views.chapter_detail, name='chapter_detail'),
    path('chapter/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
    path('make-choice/', views.make_choice, name='make_choice'),
    path('ending/<int:chapter_id>/', views.ending, name='ending'),
    path('restart/', views.restart_story, name='restart'),
    path('progress/', views.progress_history, name='progress_history'),

    # API endpoints
    path('api/stats/', views.api_reader_stats, name='api_reader_stats'),
]
