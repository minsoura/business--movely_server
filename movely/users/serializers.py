from rest_framework import routers, serializers, viewsets
from movely.users.models import *
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
from user_media.serializers import MediaSerializer


class ProfileSerializer(serializers.ModelSerializer):
    medias = MediaSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'school', 'major', 'job', 'company',
                  'personality', 'region', 'height', 'body_type', 'media_ids', "medias")


class UserSerializer(serializers.ModelSerializer):
    # profiles = serializers.PrimaryKeyRelatedField(
    #     queryset=UserProfile.objects.filter(active=True), pk_field="user_id")
    # profile = ProfileSerializer()
    medias = MediaSerializer(many=True, read_only=True)
    # profile = serializers.SerializerMethodField()
    #     queryset=UserProfile.objects.filter(active=True))

    def get_profile(self, object):
        qs = UserProfile.objects.filter(active=True).first()
        serializer = ProfileSerializer(instance=qs)
        return serializer.data

    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)
        return user

    # def update(self, instance, validated_data):
    #     print('-------')
    #     print(validated_data)
    #     instance.media_ids = validated_data.get("media_ids", "[]")
    #     instance.save()
    #     return instance

    # def __init__(self, *args, **kwargs):
    #     print(kwargs)
    #     print(args)
    #     pass

    class Meta:
        model = User
        # depth = 2
        fields = ('id', 'email', 'username', 'gender', 'password',
                  'birthday', 'point', 'heart', 'school', 'major', 'job', 'company', 'personality', 'region', 'height', 'body_type', 'media_ids', 'active', "medias")
