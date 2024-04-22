from rest_framework import serializers
from .models import Post, Rating
from django.utils import timezone


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), write_only=True)

    class Meta:
        model = Rating


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'slug', 'average_rating', 'author', 'body',
                  'publish', 'created', 'updated', 'status']
        read_only_fields = ['id',  'author', 'slug',
                            'average_rating', 'created', 'updated']

    def validate(self, data):
        if 'publish' in data and data['publish'] < timezone.now():
            raise serializers.ValidationError(
                "Publish date must be in the future.")
        return data
