# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20160530_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('N', 'Not specified'), ('M', 'Male')], default='N', max_length=1),
        ),
    ]
