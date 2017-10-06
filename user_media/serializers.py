from rest_framework import routers, serializers, viewsets
from .models import Media
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings


class MediaSerializer(serializers.ModelSerializer):
    media_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = (
            'media', 'type', 'thumbnail', 'media_url', 'id', 'thumbnail_url')

    def get_media_url(self, obj):
        return settings.ROOT_URL + obj.media.url

    def get_thumbnail_url(self, obj):
        return settings.ROOT_URL + obj.thumbnail.url
