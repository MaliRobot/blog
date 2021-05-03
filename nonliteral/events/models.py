from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from location_field.models.plain import PlainLocationField

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, default='Belgrade')
    location = PlainLocationField(based_fields=['city'], default='44.815971791260516,20.46053409576416', zoom=2, blank=True)
    show_map = models.BooleanField()
    start = models.DateTimeField(default=timezone.now, blank=False)
    end = models.DateTimeField(blank=True, null=True)
    public = models.BooleanField()

    class Meta:
        db_table = "events"

    def __str__(self):
        return self.name

