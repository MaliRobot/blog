from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from meta.models import ModelMeta
from ckeditor.fields import RichTextField

# Create your models here.


class Node(models.Model):
    name = models.CharField(max_length=255)
    text = RichTextField()
    prev = models.ForeignKey('self', related_name='back', on_delete=models.CASCADE, null=True)
    next = models.ForeignKey('self', related_name='forward', on_delete=models.CASCADE, null=True)

    nonlinear = models.ForeignKey('ChoiceNode', related_name='nonelinear_switch', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class ChoiceNode(Node):
    high = models.ForeignKey('self', related_name='good', on_delete=models.CASCADE, null=True)
    mid = models.ForeignKey('self', related_name='neutral', on_delete=models.CASCADE, null=True)
    low = models.ForeignKey('self', related_name='bad', on_delete=models.CASCADE, null=True)

    linear = models.ForeignKey('Node', related_name='linear_switch', on_delete=models.CASCADE, null=True)

    def get_high(self):
        return self.high

    def get_mid(self):
        return self.mid

    def get_low(self):
        return self.low



