from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class NewsSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=None)
    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'timeCreate', 'author', 'tags', 'archive')


class TagsSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=None)
    class Meta:
        model = Tags
        fields = ('id', 'name')


class AuthorsSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=None)
    class Meta:
        model = Author
        fields = ('id', 'name')


class AuthorsAdminSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=None)
    class Meta:
        model = Author
        fields = ('id', 'user', 'name')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
        }
        def create(self, validated_data):
            user = User.objects.create_user(
                validated_data['username'],
                password=validated_data['password'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                email=validated_data['email']
            )
            return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class NewsNotAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsNotAuthor
        fields = ('id', 'title', 'content', 'timeCreate', 'user', 'tags', 'nameAuthor')