from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db import models

# Create your models here.


class Poem(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()
    public = models.BooleanField()
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now, blank=False)

    class Meta:
        db_table = "poems"

    def __str__(self):
        return self.title
