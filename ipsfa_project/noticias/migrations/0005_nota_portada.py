# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_auto_20170106_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='notas'),
        ),
    ]