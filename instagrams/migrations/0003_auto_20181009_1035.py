# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-09 07:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagrams', '0002_auto_20181006_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
