from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'description', 'address', 'city', 'location', 'start', 'end', 'public']
