# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-30 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0006_auto_20200330_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
