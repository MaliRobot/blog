from django.shortcuts import render
from .models import About
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def about(request):
    about = About.objects.get(pk=1)
    template = loader.get_template('about.html')
    context = {
        'about': about,
    }
    return HttpResponse(template.render(context, request))
