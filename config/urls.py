# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from movely.users.views import UserViewSet
from rest_framework import routers, serializers, viewsets
from movely.users.models import User
from movely.users.views import UserViewSet
from user_media.views import UserMediaViewSet
from card.views import CardViewSet
from message.views import MessageViewSet
from point.views import PointPolicyViewSet, PointHistoryViewSet
from ideal_style.views import IdealStyleViewSet

urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name='pages/home.html'), name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include('movely.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),

    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Serializers define the API representation.


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cards', CardViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'pointpolicies', PointPolicyViewSet)
router.register(r'pointhistories', PointHistoryViewSet)
router.register(r'idealstyles', IdealStyleViewSet)
router.register(r'medias', UserMediaViewSet, base_name="media")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api/', include(router.urls)),

]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
