from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import News, Post, Album, Poem, Event
from .forms import ContactForm
from rest_framework import viewsets
from .serializers import NewsSerializer, PostSerializer, AlbumSerializer, PoemSerializer, EventSerializer
from rest_framework.pagination import CursorPagination


def index(request):
    news_articles = News.objects.filter(public=True).order_by('-date_published')
    page = request.GET.get('page', 1)
    paginator = Paginator(news_articles, 5)
    template = loader.get_template('index.html')
    news = paginator.page(page)
    posts = Post.objects.filter(public=True).order_by('-date_published')[:10]
    context = {
        'news': news,
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))


def blog(request):
    posts = Post.objects.filter(public=True).order_by('-date_published')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    blog_posts = paginator.page(page)
    template = loader.get_template('blog.html')
    news = News.objects.filter(public=True).order_by('-date_published')[:10]
    context = {
        'blog_posts': blog_posts,
        'news': news,
    }
    return HttpResponse(template.render(context, request))


def poems(request):
    poems = Poem.objects.filter(public=True).order_by('-date_created')
    template = loader.get_template('poems.html')
    context = {
        'poems': poems,
    }
    return HttpResponse(template.render(context, request))


def single_post(request, pk):
    post = get_object_or_404(Post, public=True, pk=pk)
    posts = Post.objects.filter(public=True).exclude(pk=pk).order_by('-date_published')[:10]
    template = loader.get_template('single_blogpost.html')

    context = {
        'post': post,
        'posts': posts,
        'meta': post.as_meta(),
    }
    return HttpResponse(template.render(context, request))


def releases(request):
    albums = Album.objects.order_by('-release_date')
    template = loader.get_template('releases.html')
    context = {
        'albums': albums,
    }
    return HttpResponse(template.render(context, request))


def events(request):
    events_all = Event.objects.filter(public=True).order_by('-start')
    page = request.GET.get('page', 1)
    paginator = Paginator(events_all, 5)
    events = paginator.page(page)
    template = loader.get_template('events.html')
    news = News.objects.filter(public=True).order_by('-date_published')[:10]
    context = {
        'events': events,
        'news': news,
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


def about(request):
    return render(request, 'about.html')


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint for news.
    """
    queryset = News.objects.filter(public=True).order_by('-date_published')
    serializer_class = NewsSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for posts.
    """
    queryset = Post.objects.filter(public=True).order_by('-date_published')
    serializer_class = PostSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint for albums.
    """
    queryset = Album.objects.filter(public=True).order_by('-release_date')
    serializer_class = AlbumSerializer


class PoemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for poems.
    """
    queryset = Poem.objects.filter(public=True).order_by('-date_created')
    serializer_class = PoemSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint for events.
    """
    queryset = Event.objects.filter(public=True).order_by('start')
    serializer_class = EventSerializer


