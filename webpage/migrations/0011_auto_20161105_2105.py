# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0010_auto_20161105_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='notes',
            new_name='mobile',
        ),
        migrations.RemoveField(
            model_name='data',
            name='done',
        ),
        migrations.AddField(
            model_name='data',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='images_details',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='images',
            name='images',
            field=models.CharField(max_length=200),
        ),
    ]
