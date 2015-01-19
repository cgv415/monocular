# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_Corto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(blank=True, max_length=30, null=True, choices=[(b'seleccionado', b'Seleccionado'), (b'premiado', b'Premiado')])),
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
                ('anyo', models.PositiveIntegerField(verbose_name='a\xf1o')),
                ('fecha', models.CharField(max_length=100, null=True, blank=True)),
                ('web', models.URLField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to=b'galeria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('portfolio', models.BooleanField()),
                ('titulo', models.CharField(max_length=100)),
                ('anyo', models.PositiveIntegerField(null=True, verbose_name='a\xf1o', blank=True)),
                ('duracion', models.CharField(max_length=100, null=True, blank=True)),
                ('soporte', models.CharField(max_length=100, null=True, blank=True)),
                ('formato', models.CharField(max_length=100, null=True, blank=True)),
                ('director', models.CharField(max_length=100, null=True, blank=True)),
                ('productora', models.CharField(max_length=100, null=True, blank=True)),
                ('reparto', models.CharField(max_length=100, null=True, blank=True)),
                ('sinopsis', models.TextField()),
                ('pais', models.CharField(max_length=100, null=True, blank=True)),
                ('genero', models.CharField(max_length=100, null=True, blank=True)),
                ('trailer', models.TextField(null=True, blank=True)),
                ('imagen', models.ImageField(upload_to=b'cortometrajes')),
                ('cliente', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'publicidadgallery')),
                ('video', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='servicio',
            field=models.ManyToManyField(to='servicios.Servicio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='galeria',
            name='proyecto',
            field=models.ForeignKey(to='servicios.Proyecto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estado_corto',
            name='corto',
            field=models.ForeignKey(to='servicios.Proyecto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estado_corto',
            name='festival',
            field=models.ForeignKey(to='servicios.Festival'),
            preserve_default=True,
        ),
    ]
