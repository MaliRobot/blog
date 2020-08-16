from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Image, Order, Album, News, About, Poem, Event

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Order)
admin.site.register(Album)
admin.site.register(News)
admin.site.register(About)
admin.site.register(Poem)
admin.site.register(Event)
