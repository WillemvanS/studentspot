# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-09 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status1', models.CharField(max_length=3)),
                ('status2', models.CharField(max_length=3)),
                ('status3', models.CharField(max_length=3)),
                ('status4', models.CharField(max_length=3)),
                ('status5', models.CharField(max_length=3)),
                ('status6', models.CharField(max_length=3)),
                ('status7', models.CharField(max_length=3)),
                ('status8', models.CharField(max_length=3)),
                ('status9', models.CharField(max_length=3)),
                ('status10', models.CharField(max_length=3)),
                ('status11', models.CharField(max_length=3)),
                ('status12', models.CharField(max_length=3)),
                ('status13', models.CharField(max_length=3)),
                ('status14', models.CharField(max_length=3)),
                ('status15', models.CharField(max_length=3)),
                ('status16', models.CharField(max_length=3)),
                ('status17', models.CharField(max_length=3)),
                ('status18', models.CharField(max_length=3)),
                ('status19', models.CharField(max_length=3)),
                ('status20', models.CharField(max_length=3)),
            ],
        ),
    ]
