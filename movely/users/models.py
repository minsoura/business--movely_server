# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from base.models import *
from django.utils import timezone
import ast
from .exceptions import *
from datetime import datetime
from datetime import date
from card.models import Card
from user_media.models import Media


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    # nickname = models.CharField(
    #     _('nickname of User'), blank=True, max_length=255)
    REQUIREMENT_GET_NEXT_HEART = 1
    REQUIREMENT_GET_IDEAL_HEART = 2
    point = models.PositiveIntegerField(default=30)
    heart = models.IntegerField(default=3)
    last_heart_update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def create_next_card(self):
        if self.heart < User.REQUIREMENT_GET_NEXT_HEART:
            raise HeartNotEnoughException()
        self.heart = self.heart - User.REQUIREMENT_GET_NEXT_HEART
        self.save()
        if self.gender == "M":
            opposite_gender = "F"
        else:
            opposite_gender = "M"

        partner = User.objects.filter(gender=opposite_gender).first()
        if not partner:
            self.heart = self.heart + User.REQUIREMENT_GET_NEXT_HEART
            self.save()
            raise NoPartnerException()
        card = Card(user=self, partner=partner, introduce_date=date.today())
        card.save()
        return card

    # it must go to profile..
    GENDER_CHOICES = (
        ("M", "male"),
        ("F", 'female'),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='M')
    birthday = models.DateField()

    school = models.CharField(max_length=255, blank=True)
    major = models.CharField(max_length=255, blank=True)
    job = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    personality = models.CharField(max_length=255, blank=True)
    REGION_CHOICES = (
        ("SE", '서울'),
        ("KKI", '경기 - 일산'),
        ("KKU", '경기 - 의정부'),
        ("KKA", '경기 - 안양'),
        ("KKB", '경기 - 분당'),
        ("KKS", '경기 - 수원'),
        ("KKE", '경기 - 기타'),
        ("IC", '인천'),
        ("KW", '강원'),
        ("CB", '충북'),
        ("CN", '충남'),
        ("DJ", '대전'),
        ("KB", '경북'),
        ("DG", '대구'),
        ("KN", '경남'),
        ("BS", '부산'),
        ("US", '울산'),
        ("JB", '전북'),
        ("JN", '전남'),
        ("KJ", '광주'),
        ("JJ", '제주'),
    )
    region = models.CharField(
        max_length=3, choices=REGION_CHOICES)
    height = models.PositiveIntegerField(null=True)
    body_type = models.CharField(max_length=255, blank=True)
    media_ids = models.CharField(max_length=255, default="[]")
    active = models.BooleanField(default=True)

    @property
    def medias(self):
        media_ids = ast.literal_eval(self.media_ids)
        medias = Media.objects.filter(id__in=media_ids)
        return sorted(medias, key=lambda i: media_ids.index(i.pk))


class UserProfile(CommonModel):

    user = models.OneToOneField(User, related_name="profile")


# class UserIdealStyle(CommonModel):
#     user = models.ForeignKey(User, related_name="style")
#     school = models.CharField(max_length=255)
#     major = models.CharField(max_length=255, blank=True)
#     job = models.CharField(max_length=255, blank=True)
#     personality = models.CharField(max_length=255)
#     region = models.CharField(max_length=255)
#     height = models.PositiveIntegerField()
#     body_type = models.CharField(max_length=255)
#     birthday = models.DateField(default=timezone.now()) #나이 계산 목적


#     def create_ideal_style_card(self):
#         if self.user.heart < User.REQUIREMENT_GET_IDEAL_HEART:
#             raise HeartNotEnoughException()
#         self.user.heart = self.user.heart - User.REQUIREMENT_GET_IDEAL_HEART
#         self.save()
#         if self.user.gender == "M":
#             opposite_gender = "F"
#         else:
#             opposite_gender = "M"
#         partner = User.objects.filter(
#             gender=opposite_gender,
#             school=school,
#             major=major,
#             job=job,
#             personality=personality,
#             region=region,
#             height=height,
#             body_type=body_type,
#             birthday=birthday
#             ).first()
#         if not partner:
#             self.user.heart = self.user.heart + User.REQUIREMENT_GET_IDEAL_HEART
#             self.save()
#             raise NoPartnerException()
#         print(partner)
#         1 / 0
#         card = Card(user=self.user, partner=partner, introduce_date=date.today())
#         card.save()
#         return card


# organization = models.ForeignKey("organization.Organization",
#                                      verbose_name=_("organization"), on_delete=models.SET_NULL, null=True)
    # business = models.OneToOneField(
    #       "business.Business", related_name="profile")
    #   name = models.CharField(max_length=150)
    #   business_start_date = models.DateField(null=True)
    #   tax_id_issued_date = models.DateField(null=True)
    #   # 일단 string으로 받는다.
    #   business_category = models.CharField(max_length=250, blank=True)
    #   business_subcategory = models.CharField(max_length=250, blank=True)
    #   subject_to_vat = models.CharField(
    #       max_length=1, choices=VAT_TYPE_CHOICE, default='C')
    #   corporate_registration_id = models.CharField(max_length=100)
    #   tax_id = models.CharField(max_length=30)
    #   established_date = models.DateField(null=True)
    #   accounting_month = models.CharField(max_length=2)
    #   trade_name = models.CharField(max_length=100)
    #   nickname = models.CharField(max_length=100)
    #   logo_img = models.ImageField(blank=True, upload_to="business/logo")
    #   seal_img = models.ImageField(blank=True, upload_to="business/seal")
    #   address1 = models.CharField(max_length=250, blank=True)
