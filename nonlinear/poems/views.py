from django.shortcuts import render
from .models import Poem
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .serializers import PoemSerializer
# Create your views here.


def poems(request):
    poems = Poem.objects.filter(public=True).order_by('-date_created')
    template = loader.get_template('poems.html')
    context = {
        'poems': poems,
    }
    return HttpResponse(template.render(context, request))


class PoemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for poems.
    """
    queryset = Poem.objects.filter(public=True).order_by('-date_created')
    serializer_class = PoemSerializer
