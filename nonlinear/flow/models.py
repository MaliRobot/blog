from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from tagging.registry import register
from ckeditor.fields import RichTextField

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to= settings.BASE_DIR + '/images')

class Post(models.Model):
    title = models.CharField(max_length=255)
    lead = models.CharField(max_length=255)
    text = RichTextField()
    author = models.OneToOneField(User)
    public = models.BooleanField()
    language = models.CharField(max_length=3, default='eng')
    images = models.ForeignKey(Image, on_delete=models.CASCADE)
    date_published = models.DateTimeField('date published')

class Comment(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.CharField(max_length=255)
    public = models.BooleanField(default=True)
    date_posted = models.DateTimeField('date posted', blank=False)
    post = models.ForeignKey(Post, related_name='comments')

class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    description = models.TextField()
    code = models.CharField(max_length=12)
    release_date = models.DateTimeField('release date')
    images = models.ForeignKey(Image, on_delete=models.CASCADE)

class Order(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    package = models.TextField()
    date_ordered = models.DateTimeField('date ordered', blank=False)

register(Post)



