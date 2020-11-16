from django.db import models

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField()

    class Meta:
        db_table = "images"

    def __str__(self):
        return self.name