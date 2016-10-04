# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appFellas', '0002_auto_20161004_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='author', to='appFellas.User'),
        ),
        migrations.AddField(
            model_name='image',
            name='uploaded',
            field=models.DateTimeField(auto_now=True),
        ),
    ]