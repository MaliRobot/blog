from django.db import models

# Create your models here.


class About(models.Model):
    text = models.TextField()

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
