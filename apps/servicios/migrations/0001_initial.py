# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('sinopsis', models.TextField()),
                ('duracion', models.CharField(max_length=50)),
                ('anyo', models.DateField()),
                ('pais', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('reparto', models.CharField(max_length=50)),
                ('productora', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('trailer', models.CharField(max_length=150, null=True)),
                ('imagen', models.ImageField(upload_to=b'cortometrajes')),
                ('cliente', models.OneToOneField(to='administracion.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado_Corto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(blank=True, max_length=30, null=True, choices=[(b'seleccionado', b'Seleccionado'), (b'premiado', b'Premiado')])),
                ('corto', models.OneToOneField(to='servicios.Corto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('anyo', models.PositiveIntegerField()),
                ('fecha', models.CharField(max_length=100, null=True, blank=True)),
                ('web', models.URLField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='estado_corto',
            name='festival',
            field=models.OneToOneField(to='servicios.Festival'),
            preserve_default=True,
        ),
    ]
