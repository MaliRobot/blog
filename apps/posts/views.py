import re

from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Q, Func, F, Value, TextField
from django.forms import CharField

from .models import Post
from apps.news.models import News
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
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
    template = loader.get_template('post_search_results.html')
    search = request.GET.get("q")
    if search:
        search_terms = search.split()
        query = Q()
        for term in search_terms:
            query |= Q(title__icontains=term) | Q(text__icontains=term)

        posts = Post.objects.filter(
            query
        ).order_by('-date_published')
    else:
        posts = Post.objects.none()
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