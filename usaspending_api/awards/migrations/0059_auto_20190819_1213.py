# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-19 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0058_auto_20190815_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subaward',
            name='latest_transaction_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]