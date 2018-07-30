from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import News, Post, Album
from .forms import ContactForm


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


def single_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'single_post.html', {'post': post})


def releases(request):
    albums = Album.objects.order_by('-release_date')
    template = loader.get_template('releases.html')
    context = {
        'albums': albums,
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