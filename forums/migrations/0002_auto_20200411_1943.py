# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-11 18:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Forums',
            new_name='Forum',
        ),
    ]
