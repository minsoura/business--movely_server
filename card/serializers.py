from rest_framework import routers, serializers, viewsets
from .models import *
from movely.users.serializers import *


class CardSerializer(serializers.ModelSerializer):
    # partner = UserSerializer()
    # user = UserSerializer()

    class Meta:
        model = Card
        # depth = 1
        fields = ('id', 'status','introduce_date', 'partner', 'user')
