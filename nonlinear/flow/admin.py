from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Image, Order, Album, News, About, Poem, Event, AccessLog


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'language', 'date_published')


class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'data', 'ip_address', 'timestamp')


class PoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'start', 'end')


admin.site.register(News, NewsAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Poem, PoemAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(AccessLog, AccessLogAdmin)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Order)
admin.site.register(Album)
admin.site.register(About)

