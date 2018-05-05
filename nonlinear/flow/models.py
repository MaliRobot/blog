from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to= 'static/images/')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    lead = models.CharField(max_length=255)
    text = RichTextField()
    author = models.OneToOneField(User, on_delete="")
    public = models.BooleanField()
    language = models.CharField(max_length=3, default='eng')
    images = models.ForeignKey(Image, on_delete=models.CASCADE)
    date_published = models.DateTimeField('date published')

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.CharField(max_length=255)
    public = models.BooleanField(default=True)
    date_posted = models.DateTimeField('date posted', blank=False)
    post = models.ForeignKey(Post, related_name='comments', on_delete="")

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()
    public = models.BooleanField()
    language = models.CharField(max_length=3, default='eng')
    image = models.ImageField(upload_to= 'static/images/', default=None)
    date_published = models.DateTimeField('date published')

    class Meta:
        verbose_name_plural = "news"

    def __str__(self):
        return self.title


class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    description = models.TextField()
    code = models.CharField(max_length=12)
    release_date = models.DateTimeField('release date')
    images = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    package = models.TextField()
    date_ordered = models.DateTimeField('date ordered', blank=False)

    def __str__(self):
        return self.name





