# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-29 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=b'', verbose_name='default.png'),
        ),
    ]
