# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-02 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0011_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
