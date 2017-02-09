# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-08 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0018_auto_20170208_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rango',
            name='rango',
            field=models.CharField(blank=True, choices=[('--', '--'), ('G/F.', 'General en Jefe'), ('G/D.', 'General de Divicion'), ('G/B.', 'General de Brigada'), ('CNEL.', 'Coronel'), ('TCNEL.', 'Teniente Coronel'), ('MY.', 'Mayor'), ('CAP.', 'Capitan'), ('TTE.', 'Teniente'), ('AL.', 'Almirante'), ('V/A.', 'Vicealmirante'), ('C/A.', 'Contralmirante'), ('C/N.', 'Capitan de Navio'), ('C/F.', 'Capitan de Fragata'), ('C/C.', 'Capitan de Corbeta'), ('T/N.', 'Teniente de Navio'), ('T/F.', 'Teniente de Fragata')], max_length=6, null=True),
        ),
    ]