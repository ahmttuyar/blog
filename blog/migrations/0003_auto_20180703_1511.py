# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-03 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180703_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='aurtor',
            new_name='author',
        ),
    ]
