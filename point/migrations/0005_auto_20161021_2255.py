# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-21 13:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0004_auto_20161021_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pointhistory',
            old_name='point_change',
            new_name='changed_point',
        ),
    ]
