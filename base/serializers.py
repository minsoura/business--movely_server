
from rest_framework import routers, serializers, viewsets
from movely.users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        depth = 1
        fields = ('active_profile', 'nickname')
