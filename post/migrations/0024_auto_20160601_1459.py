# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 12:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_auto_20160601_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 14, 59, 15, 843000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 14, 59, 15, 842000)),
        ),
    ]
