# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_gallerypost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerypost',
            name='GalleryPost_image',
            field=models.ImageField(height_field=300, upload_to='files/galleryimages', width_field=300),
        ),
    ]
