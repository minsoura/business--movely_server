# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-15 17:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20161016_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 10, 15, 17, 23, 6, 876288, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='useridealstyle',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 10, 15, 17, 23, 6, 886288, tzinfo=utc)),
        ),
    ]
