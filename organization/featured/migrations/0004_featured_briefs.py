# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-magazine', '0009_brief_sort_order'),
        ('organization-featured', '0003_remove_featured_briefs'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured',
            name='briefs',
            field=models.ManyToManyField(blank=True, related_name='featured', to='organization-magazine.Brief', verbose_name='briefs'),
        ),
    ]