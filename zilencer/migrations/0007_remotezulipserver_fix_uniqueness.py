# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-30 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zilencer', '0006_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remotezulipserver',
            name='hostname',
            field=models.CharField(max_length=128),
        ),
    ]