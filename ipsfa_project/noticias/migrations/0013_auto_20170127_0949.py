# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-27 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0012_auto_20170127_0917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beneficiodocumento',
            options={'verbose_name': 'Documento', 'verbose_name_plural': 'Documento'},
        ),
        migrations.AlterField(
            model_name='beneficio',
            name='dependencia',
            field=models.CharField(max_length=4),
        ),
    ]
