# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]