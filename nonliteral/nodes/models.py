from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from meta.models import ModelMeta

# Create your models here.


class Node(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name