from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
from meta.models import ModelMeta

# Create your models here.


class Node(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
