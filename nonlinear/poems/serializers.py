from .models import Poem
from rest_framework import serializers


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ['title', 'text', 'public', 'author', 'date_created']