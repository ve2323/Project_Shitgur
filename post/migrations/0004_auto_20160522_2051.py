# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20160518_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerypost',
            name='GalleryPost_image',
            field=models.FileField(upload_to='files/galleryimages'),
        ),
    ]