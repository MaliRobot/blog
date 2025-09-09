from django.http import HttpResponse
from django.core.paginator import Paginator
from django.template import loader
from django.shortcuts import render
from news.models import News
from posts.models import Post
from events.models import Event
from django.views.generic import ListView
import datetime
from itertools import chain


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


class SearchView(ListView):
    template_name = 'search_results.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            blog_results = Post.objects.search(query)
            news_results = News.objects.search(query)

            queryset_chain = chain(
                blog_results,
                news_results,
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.date_published,
                        reverse=True)
            self.count = len(qs)
            return qs
        return Post.objects.none()  # just an empty queryset as default


def error_404_view(request, exception):
    template = loader.get_template('error404.html')
    return HttpResponse(template.render({}, request))


def error_505_view(request):
    template = loader.get_template('error505.html')
    return HttpResponse(template.render({}, request))
