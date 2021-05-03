from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()
    public = models.BooleanField()
    language = models.CharField(max_length=3, default='eng')
    image = models.ImageField(upload_to='static/images/', blank=True, default=None)
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFit(400, 200)],
                                      format='JPEG',
                                      options={'quality': 60})
    date_published = models.DateTimeField('date published')

    class Meta:
        verbose_name_plural = "news"
        db_table = "news"

    def __str__(self):
        return self.title

