from rest_framework import routers, serializers, viewsets
from .models import *
from movely.users.serializers import *


class PointPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PointPolicy
        # depth = 1
        fields = ('id','point_change', 'policy_description')


class PointHistorySerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = PointHistory
        # depth = 1
        fields = ('user', 'changed_point', 'point_policy', 'created_at')