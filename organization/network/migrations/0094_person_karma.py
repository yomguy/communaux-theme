# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-05-17 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0093_auto_20170301_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='karma',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
