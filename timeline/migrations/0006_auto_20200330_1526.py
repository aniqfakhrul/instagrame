# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-30 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0005_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=b''),
        ),
    ]