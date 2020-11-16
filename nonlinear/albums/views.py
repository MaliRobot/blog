from django.shortcuts import render
from .models import Album
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .serializers import AlbumSerializer
# Create your views here.


def releases(request):
    albums = Album.objects.order_by('-release_date')
    template = loader.get_template('/templates/releases.html')
    context = {
        'albums': albums,
    }
    return HttpResponse(template.render(context, request))


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint for albums.
    """
    queryset = Album.objects.filter(public=True).order_by('-release_date')
    serializer_class = AlbumSerializer
