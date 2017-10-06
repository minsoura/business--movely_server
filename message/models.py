from django.db import models
from django.conf import settings
from base.models import *
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Message(CommonModel):

    card = models.OneToOneField("card.Card")
    content = models.TextField()
    STATUS_CHOICES = (
        ("U", "unread"),
        ("R", "read"),
    )
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default="U")
    read_at = models.DateTimeField(default=None)
