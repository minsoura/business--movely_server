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
from movely.users.exceptions import *
from datetime import datetime
from datetime import date
from card.models import Card

from movely.users.models import User, UserProfile


# Create your models here.


class UserIdealStyle(CommonModel):
    user = models.ForeignKey(User, related_name="style")
    school = models.CharField(max_length=255)
    major = models.CharField(max_length=255, blank=True)
    job = models.CharField(max_length=255, blank=True)
    personality = models.CharField(max_length=255)
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
    height = models.PositiveIntegerField()
    body_type = models.CharField(max_length=255)
    AGE_CHOICES = (
        ("NP", "상관 없음"),
        ("4P", '4살 이상 연상'),
        ("13P", '1~3살 연상'),
        ("SA", '동갑'),
        ("13M", '1~3살 연하'),
        ("4M", '4살 이상 연하'),
    )
    age = models.CharField(
        max_length=3, choices=AGE_CHOICES)

    def create_ideal_style_card(self):
        if self.user.heart < User.REQUIREMENT_GET_IDEAL_HEART:
            raise HeartNotEnoughException()
        self.user.heart = self.user.heart - User.REQUIREMENT_GET_IDEAL_HEART
        self.save()
        if self.user.gender == "M":
            opposite_gender = "F"
        else:
            opposite_gender = "M"
        partner = User.objects.filter(
            gender=opposite_gender,
            school=school,
            major=major,
            job=job,
            personality=personality,
            region=region,
            height=height,
            body_type=body_type,
            age=age
        ).first()
        if not partner:
            self.user.heart = self.user.heart + \
                User.REQUIREMENT_GET_IDEAL_HEART
            self.save()
            raise NoPartnerException()
        print(partner)
        1 / 0
        card = Card(
            user=self.user, partner=partner, introduce_date=date.today())
        card.save()
        return card
