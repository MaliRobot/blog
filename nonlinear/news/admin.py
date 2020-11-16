from django.contrib import admin
from .models import  News

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')


admin.site.register(News, NewsAdmin)

