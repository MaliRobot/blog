from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from meta.models import ModelMeta
from taggit.managers import TaggableManager
from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField()

    def __str__(self):
        return self.name


class Post(ModelMeta, models.Model):
    title = models.CharField(max_length=255)
    lead = models.CharField(max_length=255)
    text = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField()
    language = models.CharField(max_length=3, default='eng')
    image = models.ImageField(upload_to='static/images/', blank=True, default=None)
    date_published = models.DateTimeField('date published')
    tags = TaggableManager()

    _metadata = {
        'title': 'title',
        'author': 'author',
        'description': 'lead',
        'image': 'get_meta_image',
    }

    def get_meta_image(self):
        if self.image:
            return self.image.url

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
    image = models.ImageField(upload_to='static/images/', blank=True, default=None)
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
    release_date = models.DateField('release date')
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    public = models.BooleanField()

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    package = models.TextField()
    date_ordered = models.DateTimeField('date ordered', blank=False)

    def __str__(self):
        return self.name


class Poem(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()
    public = models.BooleanField()
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255, default='Belgrade')
    location = PlainLocationField(based_fields=['city'], default='44.815971791260516,20.46053409576416', zoom=2)
    show_map = models.BooleanField()
    start = models.DateTimeField(default=timezone.now, blank=False)
    end = models.DateTimeField(default=timezone.now, blank=True)
    public = models.BooleanField()

    def __str__(self):
        return self.name


class About(models.Model):
    text = models.TextField()

    def __str__(self):
        return "about"

    def save(self, *args, **kwargs):
        self.pk = 1
        super(About, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


