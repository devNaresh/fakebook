__author__ = 'naresh'

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Posts, Comments


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post... Convert JSON to python object and save to model

     --- Methods ---

    1)  create() : Override default method of model serializer for user field.

    """

    class Meta:
        model = Posts
        fields = ("text",)

    def create(self, validated_data):
        validated_data["user"] = self.context['request'].user
        return super(PostSerializer, self).create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment... Convert JSON to python object and save to model

     --- Methods ---

    1)  create() : Override default method of model serializer for user field.

    """

    class Meta:
        model = Comments
        fields = ("text", "post")

    def create(self, validated_data):
        validated_data["user"] = self.context['request'].user
        return super(CommentSerializer, self).create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model... Convert JSON to python object and save to model

     --- Methods ---

    1)  create() : Override default method to save user.

    """

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password", "email")
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        username = validated_data.pop("username")
        return User.objects.create_user(username, **validated_data)
