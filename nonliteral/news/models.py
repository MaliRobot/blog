from django.db import models
from django.db.models import Q
from django.urls import reverse
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

# Create your models here.


class NewsManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(text__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct()
        return qs


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

    objects = NewsManager()

    class Meta:
        verbose_name_plural = "news"
        db_table = "news"

    def get_absolute_url(self):
        return reverse('single_news', args=[str(self.id)])

    def __str__(self):
        return self.title

