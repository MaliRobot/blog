from .models import News, Post, Poem, Album
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'text', 'image', 'public', 'date_published']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'lead', 'text', 'author', 'image', 'language', 'date_published']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'artist', 'description', 'code', 'release_date', 'image']


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ['title', 'text', 'public', 'author', 'date_created']


