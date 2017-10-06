from django.db import models
from base.models import *
from django.conf import settings
# Create your models here.

# user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)


class Media(CommonModel):
    media = models.FileField(upload_to='uploads/medias/')
    thumbnail = models.FileField(
        upload_to='uploads/thumbnails/', blank=True, default="")
    type = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="all_medias", null=True)
