from .models import Event
from news.models import News
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.template import loader
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import EventSerializer
# Create your views here.


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


def event(request, pk):
    event = get_object_or_404(Event, public=True, pk=pk)
    template = loader.get_template('event.html')
    news = News.objects.filter(public=True).order_by('-date_published')[:10]
    context = {
        'event': event,
        'news': news,
    }
    return HttpResponse(template.render(context, request))


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint for events.
    """
    queryset = Event.objects.filter(public=True).order_by('start')
    serializer_class = EventSerializer
