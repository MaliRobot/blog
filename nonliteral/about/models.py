from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class About(models.Model):
    text = RichTextField()

    class Meta:
        db_table = "about"

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


class Contact(models.Model):
    subject = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        db_table = "contacts"

    def __str__(self):
        return "contact"
