from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import News
from rest_framework import viewsets
from .serializers import NewsSerializer
from django.http import HttpResponse
# Create your views here.


def single_news(request, pk):
    news_item = get_object_or_404(News, public=True, pk=pk)
    news = News.objects.filter(public=True).exclude(pk=pk).order_by('-date_published')[:5]
    template = loader.get_template('single_news.html')
    News.objects.filter()
    context = {
        'news_item': news_item,
        'news': news,
        'meta': news_item.as_meta(),
    }
    return HttpResponse(template.render(context, request))


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint for news.
    """
    queryset = News.objects.filter(public=True).order_by('-date_published')
    serializer_class = NewsSerializer
