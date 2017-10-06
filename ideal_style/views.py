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
from .serializers import IdealStyleSerializer

# Create your views here.


class IdealStyleViewSet(viewsets.ModelViewSet):
    queryset = UserIdealStyle.objects.all()
    serializer_class = IdealStyleSerializer
