# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-21 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0005_auto_20161021_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointhistory',
            name='point_policy',
            field=models.CharField(max_length=50),
        ),
    ]
