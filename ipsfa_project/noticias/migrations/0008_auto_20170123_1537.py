# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 19:37
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0007_sucursal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sucursal',
            options={'verbose_name': 'Sucursal', 'verbose_name_plural': 'Sucursales'},
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='telefono',
            field=models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message='El numero debe telefono debe contener 15 caracteres', regex='^(\\d{4})-(\\d{3}).(\\d{2}).(\\d{2})')]),
        ),
    ]
