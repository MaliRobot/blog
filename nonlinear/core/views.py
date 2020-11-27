from django.http import HttpResponse
from django.core.paginator import Paginator
from django.template import loader
from django.shortcuts import render
from news.models import News
from posts.models import Post
from events.models import Event
import datetime


def index(request):
    news_articles = News.objects.filter(public=True).order_by('-date_published')
    page = request.GET.get('page', 1)
    paginator = Paginator(news_articles, 5)
    template = loader.get_template('index.html')
    news = paginator.page(page)
    posts = Post.objects.filter(public=True).order_by('-date_published')[:10]
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=2)
    events = Event.objects.filter(public=True, start__gt=yesterday).order_by('-start')[:4]
    context = {
        'news': news,
        'posts': posts,
        'events': events,
    }
    return HttpResponse(template.render(context, request))



def error_404_view(request, exception):
    template = loader.get_template('error404.html')
    return HttpResponse(template.render({}, request))


def error_505_view(request):
    template = loader.get_template('error505.html')
    return HttpResponse(template.render({}, request))
