# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectes', '0002_auto_20160501_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='metrica',
            name='alerta_creada',
            field=models.IntegerField(default=0),
        ),
    ]
