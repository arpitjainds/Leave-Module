# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170831_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='comment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
