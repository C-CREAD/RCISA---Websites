from rest_framework import serializers
from .models import Sermon

class SermonSerializer(serializers.ModelSerializer):
    preacher_name = serializers.CharField(source='preacher.full_name', read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Sermon
        fields = '__all__'
        read_only_fields = ('slug', 'created_at', 'updated_at', 'likes')

    def get_likes_count(self, obj):
        return obj.likes.count()