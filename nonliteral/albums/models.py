from django.db import models
from images.models import Image
# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    description = models.TextField()
    code = models.CharField(max_length=12)
    release_date = models.DateField('release date')
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    public = models.BooleanField()

    class Meta:
        db_table = "albums"

    def __str__(self):
        return self.name

