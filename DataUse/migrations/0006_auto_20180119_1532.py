# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-19 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataUse', '0005_delete_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapull_detail',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='datapull_detail',
            name='pubtype',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
