# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20160527_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
