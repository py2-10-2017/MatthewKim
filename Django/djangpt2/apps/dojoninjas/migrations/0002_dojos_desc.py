# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojoninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]
