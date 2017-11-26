from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to= settings.BASE_DIR + '/images')

class Post(models.Model):
    title = models.CharField(max_length=255)
    lead = models.CharField(max_length=255)
    text = models.TextField()
    author = models.OneToOneField(User)
    public = models.BooleanField()
    images = models.ForeignKey(Image, on_delete=models.CASCADE)
    date_published = models.DateTimeField('date published')

