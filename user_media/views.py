# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from rest_framework import routers, serializers, viewsets
from .serializers import *
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser, FormParser, JSONParser, MultiPartParser
import sys
from moviepy.editor import VideoFileClip
import traceback
from django.conf import settings


class UserMediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    # parser_classes = (FormParser, FileUploadParser, JSONParser,)
    # parser_classes = (FileUploadParser,)
    parser_classes = (FormParser, MultiPartParser,)
    # def pre_save(self, obj):
    #     1 / 0
    #     obj.media = self.request.FILES.get('file')

    def create(self, request):
        user = request.user
        user_media = Media(user=user, media=request.FILES.get('file'))
        user_media.type = request.data['type']
        user_media.save()
        if user_media.type == "video":
            print(1)
            video_path = str(user_media.media.url)
            video_full_path = str(settings.APPS_DIR) + video_path
            print(video_full_path)
            thumbnail_path = video_path.replace(
                "medias/", "thumbnails/")[:video_path.rfind('.')] + ".jpg"
            thumbnail_full_path = str(settings.APPS_DIR) + thumbnail_path
            clip = VideoFileClip(video_full_path)
            clip.save_frame(thumbnail_full_path, t=1.00)
            print(clip)
            user_media.thumbnail = thumbnail_path
            user_media.save()
        else:
            user_media.thumbnail = str(user_media.media.url)
            user_media.save()
        return Response(MediaSerializer(user_media).data)
