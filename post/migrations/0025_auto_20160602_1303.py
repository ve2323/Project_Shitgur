# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 11:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_auto_20160601_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 2, 13, 3, 50, 623000)),
        ),
        migrations.AlterField(
            model_name='points_comment',
            name='points_comment_vote',
            field=models.CharField(choices=[('D', 'Dislike'), ('N', 'No vote'), ('L', 'Like')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_posted',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 2, 13, 3, 50, 622000)),
        ),
    ]
