# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from rest_framework import routers, serializers, viewsets
from .serializers import *
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from datetime import date
from movely.users.exceptions import *
from movely.users.models import User


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    # def me(self, request, *args, **kwargs):
    #     # User = get_user_model()
    #     # self.object = get_object_or_404(User, pk=request.user.id)
    #     serializer = self.get_serializer(request.user)
    #     a = UserSerializer(request.user)
    #     return Response(a.data)

    def list(self, request):
        cards = Card.objects.filter(user=request.user).all()
        serializer = self.get_serializer(cards, many=True)
        return Response(serializer.data)

    @list_route(permission_classes=[IsAuthenticated])
    def current(self, request, *args, **kwargs):
        card = Card.objects.current()
        serializer = self.get_serializer(card)
        return Response(serializer.data)

    @list_route(methods=['post'], permission_classes=[IsAuthenticated])
    def create_next_card(self, request):
        user = request.user
        try:
            card = user.create_next_card()
        except HeartNotEnoughException:
            return Response({"error": "not_enough_heart"}, status=501)
        except NoPartnerException:
            return Response({"error": "no partner"}, status=501)
        serializer = self.get_serializer(card)
        return Response(serializer.data)

    @list_route(methods=['post', 'get'], permission_classes=[IsAuthenticated])
    def create_ideal_style_card(self,request):
        user = request.user
        try:
            card = user.create_ideal_style_card()
        except HeartNotEnoughException:
            return Response({"error": "not_enough_heart"}, status=501)
        except NoPartnerException:
            return Response({"error": "no partner"}, status=501)
        serializer = self.get_serializer(card)
        return Response(serializer.data)
