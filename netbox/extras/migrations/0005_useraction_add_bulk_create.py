# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-04 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0004_topologymap_change_comma_to_semicolon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraction',
            name='action',
            field=models.PositiveSmallIntegerField(choices=[(1, b'created'), (7, b'bulk created'), (2, b'imported'), (3, b'modified'), (4, b'bulk edited'), (5, b'deleted'), (6, b'bulk deleted')]),
        ),
    ]
