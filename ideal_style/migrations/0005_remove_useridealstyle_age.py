# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-20 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideal_style', '0004_auto_20161020_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useridealstyle',
            name='age',
        ),
    ]
