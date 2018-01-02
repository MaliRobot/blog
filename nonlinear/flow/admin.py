from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Image, Order, Album

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Order)
admin.site.register(Album)