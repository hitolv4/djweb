# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 15:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noticias', '0005_nota_portada'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselNota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('imagen', models.ImageField(upload_to='carouselnota')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componente', models.CharField(choices=[('AV.', 'Aviacion'), ('EJ.', 'Ejercito'), ('GN.', 'Guardia Nacional'), ('AR.', 'Armada')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='GaleriaExpresidentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('imagen', models.ImageField(upload_to='galeria_expresidentes')),
                ('inicio', models.DateField(blank=True, null=True)),
                ('fin', models.DateField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Galeria de Expresidentes',
                'verbose_name_plural': 'Galeria de Expresidentes',
            },
        ),
        migrations.CreateModel(
            name='LineaDeMando',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, unique=True)),
                ('cargo', models.CharField(max_length=250)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='linea_mando')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Linea de Mando',
                'verbose_name_plural': 'Linea de Mando',
            },
        ),
        migrations.CreateModel(
            name='Militar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('imagen', models.ImageField(upload_to='militares')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.Componente')),
            ],
            options={
                'verbose_name': 'Oficial',
                'verbose_name_plural': 'Oficial',
            },
        ),
        migrations.CreateModel(
            name='Rango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rango', models.CharField(choices=[('G/F.', 'General en Jefe'), ('G/D.', 'General de Divicion'), ('G/B.', 'General de Brigada'), ('CNEL.', 'Coronel'), ('TCNEL.', 'Teniente Coronel'), ('MY.', 'Mayor'), ('CAP.', 'Capitan'), ('TTE.', 'Teniente'), ('AL.', 'Almirante'), ('VA.', 'Vicealmirante'), ('CA.', 'Contralmirante'), ('CN.', 'Capitan de Navio'), ('CF.', 'Capitan de Fragata'), ('CC.', 'Capitan de Corbeta'), ('TN.', 'Teniente de Navio'), ('TF.', 'Teniente de Fragata')], max_length=6)),
                ('componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.Componente')),
            ],
        ),
        migrations.AlterModelOptions(
            name='ultimahora',
            options={'verbose_name': 'Ultima Hora', 'verbose_name_plural': 'Ultima Hora'},
        ),
        migrations.RemoveField(
            model_name='ultimahora',
            name='texto',
        ),
        migrations.AddField(
            model_name='ultimahora',
            name='archivo',
            field=models.FileField(blank=True, upload_to='ultimahora/files'),
        ),
        migrations.AddField(
            model_name='ultimahora',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='ultimahora/images'),
        ),
        migrations.AlterField(
            model_name='nota',
            name='portada',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to='notas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nota',
            name='titulo',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='militar',
            name='rango',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='componente', chained_model_field='componente', on_delete=django.db.models.deletion.CASCADE, to='noticias.Rango'),
        ),
        migrations.AddField(
            model_name='carouselnota',
            name='nota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.Nota'),
        ),
    ]