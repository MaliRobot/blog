from django.http import HttpResponse
from django.core.paginator import Paginator
from django.template import loader
from django.shortcuts import render
from core.forms import ContactForm
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


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'contact.html', {'form': None, 'submitted': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'submitted': False})