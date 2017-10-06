# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-15 09:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20161015_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='heart',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='user',
            name='last_heart_update_datetime',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 10, 15, 9, 15, 48, 164787, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 10, 15, 9, 15, 27, 60296, tzinfo=utc)),
        ),
    ]
