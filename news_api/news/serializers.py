from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=None)
    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'timeCreate', 'author', 'tags')