from rest_framework import serializers

from .models import Poem


class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ["title", "text", "public", "author", "date_created"]
