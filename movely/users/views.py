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
import traceback


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['name', 'point']

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(permission_classes=[IsAuthenticated])
    def me(self, request, *args, **kwargs):
        # User = get_user_model()
        # self.object = get_object_or_404(User, pk=request.user.id)
        serializer = self.get_serializer(request.user)
        a = UserSerializer(request.user)
        return Response(a.data)

    # def list(self, request):
    #     pass

    def update(self, request, pk):
        user = request.user
        seralizer = UserSerializer(user, data=request.data, partial=True)
        if seralizer.is_valid():
            seralizer.save()
            user_data = seralizer.data
            # profile_data = request.data.get("profile")
            # user_data['profile'] = ProfileSerializer(profile).data
            # print(profile_data)
            # if profile_data:
            #     profile_serializer = ProfileSerializer(
            #         data=profile_data, partial=True)
            #     if profile_serializer.is_valid():
            #         user.profiles.filter(active=True).update(active=False)
            #         profile = profile_serializer.save(user=user, active=True)
            #         # print(profile_serializer.validated_data)
            #         # profile = UserProfile(profile_serializer.validated_data)
            #         # profile.active = True
            #         # profile.user = user
            #         # profile.save()
            #         user_data['profile'] = ProfileSerializer(profile).data
            #     else:
            #         print(profile_serializer.errors)
            return Response(user_data)
        else:
            return Response(seralizer.errors, status=401)

    #     print(user)
    #     print(pk)
    #     print(request.data)
    #     1 / 0
    #     pass

    # def create(self, request):
    #     pass
    # form = InvoiceForm(user=request.user, data=request.data)
    # # multi_forms = self.multi_form()
    # if form.is_valid():  # and item_form_set.is_valid():
    #     invoice = form.save()
    #     invoice_items = []
    #     for i, invoice_item in enumerate(request.data['invoice_items']):
    #         invoice_item_form = InvoiceItemForm(invoice_item)
    #         if invoice_item_form.is_valid():
    #             invoice_item = invoice_item_form.save(commit=False)
    #             invoice_item.invoice = invoice
    #             invoice_item.save()
    #             # invoice.invoice_items.add(invoice_item)
    #             # invoice_items.append(invoice)
    #         else:
    #             raise APIException(
    #                 {"invoice_items_" + str(i): invoice_item_form.errors})
    #             # return Response(
    #             #     {"invoice_items_" + str(i) : invoice_item_form.errors},
    #             #         status=status.HTTP_400_BAD_REQUEST)
    #     # invoice.save()
    #     # map((lambda x: x.save()), invoice_item.invoice_items)
    #     serializer = InvoiceSerializer(invoice)
    #     return Response(serializer.data)
    # else:
    #     raise APIException(form.errors)
