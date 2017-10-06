from django.db import models
from movely.users.models import *
from django.conf import settings
from base.models import *
from movely.users.models import User


# Create your models here.
class PointPolicy(CommonModel):
    point_change = models.IntegerField()
    policy_description = models.CharField(max_length=50)


class PointHistory(CommonModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="point_histories", null=True)
    point_policy = models.CharField(max_length=50)
    changed_point = models.IntegerField()
