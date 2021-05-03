from .models import Album
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'artist', 'description', 'code', 'release_date', 'image']
