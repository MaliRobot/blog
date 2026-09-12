from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from rest_framework import viewsets

from .models import News
from .serializers import NewsSerializer

# Create your views here.


def news_list(request):
    """List of public news items with pagination."""
    news_qs = News.objects.filter(public=True).order_by("-date_published")
    page = request.GET.get("page", 1)
    paginator = Paginator(news_qs, 10)
    news_page = paginator.page(page)
    template = loader.get_template("news_list.html")
    context = {
        "news_list": news_page,
    }
    return HttpResponse(template.render(context, request))


def single_news(request, pk):
    news_item = get_object_or_404(News, public=True, pk=pk)
    news = (
        News.objects.filter(public=True).exclude(pk=pk).order_by("-date_published")[:5]
    )
    template = loader.get_template("single_news.html")
    context = {
        "news_item": news_item,
        "news": news,
        "meta": news_item.as_meta(),
    }
    return HttpResponse(template.render(context, request))


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint for news.
    """

    queryset = News.objects.filter(public=True).order_by("-date_published")
    serializer_class = NewsSerializer
