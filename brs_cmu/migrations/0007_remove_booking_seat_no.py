# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-24 07:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brs_cmu', '0006_auto_20160420_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='seat_no',
        ),
    ]
