from ckeditor.fields import RichTextField
from meta.models import ModelMeta
from taggit.managers import TaggableManager
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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

    class Meta:
        db_table = "posts"

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

    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.title