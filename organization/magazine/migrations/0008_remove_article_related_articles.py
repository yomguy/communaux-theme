# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-24 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization-magazine', '0007_auto_20160924_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='related_articles',
        ),
    ]