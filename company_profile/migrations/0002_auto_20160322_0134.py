# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=30, unique=True, verbose_name='usuario'),
        ),
    ]