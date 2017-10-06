from django.db import models
from django.conf import settings
from base.models import *
# Create your models here.

# class CategoryQuerySet(models.QuerySet):

#     def unremoved(self):
#         return self.filter(Q(parent=None) | Q(parent__is_removed=False),
#                            is_removed=False)

#     def public(self):
#         return self.filter(is_private=False)

#     def visible(self):
#         return self.unremoved().public()

#     def opened(self):
#         return self.filter(Q(parent=None) | Q(parent__is_closed=False),
#                            is_closed=False)

#     def parents(self):
#         return self.filter(parent=None)

#     def children(self, parent):
#         if parent.is_subcategory:
#             return self.none()

#         return self.filter(parent=parent)


class CardManager(models.Manager):

    def current(self):
        return self.active().last()

    def active(self):
        return self.filter(status__in=("0", "1", "2"))


class Card(CommonModel):
    STATUS_CHOICES = (
        ("0", "발급"),
        ("1", "선택"),
        ("2", "좋아요"),
        ("8", "패스"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="cards")
    partner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="target_cards")
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default="0")
    introduce_date = models.DateField()
    objects = CardManager()

    def __str__(self):
        return self.user.username + "|" + self.partner.username
