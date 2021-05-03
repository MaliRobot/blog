from django.shortcuts import render
from rest_framework import viewsets
from .models import News
from rest_framework import viewsets
from .serializers import NewsSerializer
# Create your views here.


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint for news.
    """
    queryset = News.objects.filter(public=True).order_by('-date_published')
    serializer_class = NewsSerializer
