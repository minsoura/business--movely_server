# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-20 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideal_style', '0008_remove_useridealstyle_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='useridealstyle',
            name='age',
            field=models.CharField(choices=[('NP', '상관 없음'), ('4P', '4살 이상 연상'), ('13P', '1~3살 연상'), ('SA', '동갑'), ('13M', '1~3살 연하'), ('4M', '4살 이상 연하')], default='NP', max_length=3),
        ),
    ]