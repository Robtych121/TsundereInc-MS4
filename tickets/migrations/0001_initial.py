# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-07 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('status', models.CharField(default='', max_length=50)),
                ('priority', models.CharField(default='', max_length=50)),
                ('upvotes', models.IntegerField()),
                ('views', models.IntegerField()),
            ],
        ),
    ]
