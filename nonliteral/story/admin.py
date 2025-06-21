# story/admin.py
from django.contrib import admin
from .models import Chapter, Choice, ReaderUser, UserProgress, ChapterConnection


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_terminal', 'date_created']
    list_filter = ['is_terminal', 'date_created']
    search_fields = ['title', 'text']


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'from_chapter', 'to_chapter', 'money_cost', 'energy_cost']
    list_filter = ['from_chapter', 'to_chapter']
    search_fields = ['name', 'description']


@admin.register(ReaderUser)
class ReaderUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'money', 'energy', 'current_chapter', 'date_joined']
    list_filter = ['is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    readonly_fields = ['date_joined', 'last_login']


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['reader', 'chapter', 'choice_made', 'timestamp']
    list_filter = ['timestamp', 'reader']
    search_fields = ['reader__username', 'chapter__title']
