# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20160317_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('jobs', models.ManyToManyField(blank=True, null=True, to='jobs.Jobs')),
            ],
        ),
    ]