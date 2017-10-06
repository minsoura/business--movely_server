from rest_framework import routers, serializers, viewsets
from .models import *
from movely.users.serializers import *


class MessageSerializer(serializers.ModelSerializer):
    # partner = UserSerializer(read_only=True)

    class Meta:
        model = Message
        # depth = 2
        fields = ('id','card', 'content', 'status', 'read_at')