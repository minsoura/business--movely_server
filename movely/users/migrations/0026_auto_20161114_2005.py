# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-14 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20161114_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='active',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='body_type',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='company',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='height',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='job',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='major',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='media_ids',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='personality',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='region',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='school',
        ),
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default='1988-10-09'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='body_type',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(
                choices=[('M', 'male'), ('F', 'female')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='major',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='media_ids',
            field=models.CharField(default='[]', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='personality',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('SE', '서울'), ('KKI', '경기 - 일산'), ('KKU', '경기 - 의정부'), ('KKA', '경기 - 안양'), ('KKB', '경기 - 분당'), ('KKS', '경기 - 수원'), ('KKE', '경기 - 기타'), ('IC', '인천'), ('KW', '강원'),
                                            ('CB', '충북'), ('CN', '충남'), ('DJ', '대전'), ('KB', '경북'), ('DG', '대구'), ('KN', '경남'), ('BS', '부산'), ('US', '울산'), ('JB', '전북'), ('JN', '전남'), ('KJ', '광주'), ('JJ', '제주')], default="SE", max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
