# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-14 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.CharField(choices=[('it', 'it'), ('moto', 'moto'), ('climbing', 'climbing'), ('guitar', 'guitar'), ('blob', 'blob')], max_length=8)),
                ('title', models.CharField(max_length=140)),
                ('article_link', models.CharField(default='#', max_length=40)),
                ('author', models.CharField(max_length=40)),
                ('author_link', models.TextField(default='#')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('views_count', models.IntegerField(default=0)),
            ],
        ),
    ]
