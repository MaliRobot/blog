from django.db import models
from core.helpers import RandomFileName

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to=RandomFileName('static/images/'))

    class Meta:
        db_table = "images"

    def __str__(self):
        return self.name