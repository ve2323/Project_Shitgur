# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20160527_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='user_image',
            field=models.ImageField(default='account/media/user_images/default.jpg', upload_to='account/media/user_images'),
        ),
    ]
