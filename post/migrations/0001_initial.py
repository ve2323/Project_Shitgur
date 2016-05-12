# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_posted', models.DateTimeField(verbose_name='DateTime published')),
                ('post_text', models.TextField(max_length=2000)),
                ('post_likes', models.IntegerField(default=0)),
                ('post_dislikes', models.IntegerField(default=0)),
                ('post_image', models.FileField(upload_to='files/images')),
                ('post_tags', models.CharField(default=None, max_length=1000)),
            ],
        ),
    ]
