from rest_framework import routers, serializers, viewsets
from movely.users.models import *
from .models import *


class IdealStyleSerializer(serializers.ModelSerializer):
    age = serializers.MultipleChoiceField(choices=UserIdealStyle.AGE_CHOICES)
    region = serializers.MultipleChoiceField(choices=UserIdealStyle.REGION_CHOICES)
    class Meta:
        model = UserIdealStyle
        fields = ('user','school','major','job','personality','region','height','body_type','age')