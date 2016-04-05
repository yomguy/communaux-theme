# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0011_auto_20160323_1159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['last_name'], 'verbose_name': 'artist'},
        ),
        migrations.AddField(
            model_name='audio',
            name='featured',
            field=models.BooleanField(default=False, verbose_name='featured'),
        ),
        migrations.AddField(
            model_name='video',
            name='featured',
            field=models.BooleanField(default=False, verbose_name='featured'),
        ),
    ]
