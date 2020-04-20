# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-20 10:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20200411_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('author', models.CharField(default='', max_length=50)),
                ('ticketID', models.IntegerField(default=0)),
            ],
        ),
    ]
