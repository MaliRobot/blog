from django.shortcuts import render
from .models import Post
from news.models import News
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializers import PostSerializer

# Create your views here.


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


def search_posts(request):
    template = loader.get_template('search_results.html')
    search = request.GET.get("search")
    posts = News.objects.filter(text__contains=search).order_by('-date_published')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    blog_posts = paginator.page(page)
    context = {
        'posts': blog_posts,
    }
    return HttpResponse(template.render(context, request))


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for posts.
    """
    queryset = Post.objects.filter(public=True).order_by('-date_published')
    serializer_class = PostSerializer