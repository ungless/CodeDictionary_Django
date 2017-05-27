# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dictionary', '0004_word_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, editable=False),
            preserve_default=False,
        ),
    ]
