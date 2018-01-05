from django.http import HttpResponse
from django.template import loader
from .models import News, Post, Album

# Create your views here.
def index(request):
    news = News.objects.order_by('-date_published')[:5]
    template = loader.get_template('index.html')
    context = {
        'news': news,
    }
    return HttpResponse(template.render(context, request))

def blog(request):
    blog_posts = Post.objects.order_by('-date_published')[:5]
    template = loader.get_template('blog.html')
    context = {
        'blog_posts': blog_posts,
    }
    return HttpResponse(template.render(context, request))

def albums(request):
    albums = Album.objects.order_by('-release_date')
    template = loader.get_template('releases.html')
    context = {
        'albums': albums,
    }
    return HttpResponse(template.render(context, request))