from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.full_name', read_only=True)
    slug = serializers.SlugField(read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'slug', 'content', 'cover_image', 'author', 'likes', 'share_count', 'author_name', 'created_at', 'updated_at')
        read_only_fields = ('author', 'slug')

    def get_likes(self, obj):
        return obj.likes.count()
