# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-14 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20170114_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='article_link',
            field=models.CharField(default='#', max_length=40, unique=True),
        ),
    ]