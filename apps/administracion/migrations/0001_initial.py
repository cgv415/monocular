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
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activo', models.BooleanField(default=True)),
                ('ciudad', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activo', models.BooleanField(default=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(verbose_name='tel\xe9fono')),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=150, verbose_name='ubicaci\xf3n')),
                ('cif', models.CharField(max_length=9)),
                ('general', models.TextField(null=True, blank=True)),
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
        migrations.CreateModel(
            name='TextoDescriptivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50, choices=[(b'inicio', b'Inicio'), (b'distribucion', b'Distribucion'), (b'produccion', b'Produccion'), (b'postproduccion', b'Postproduccion'), (b'publicidad', b'Publicidad')])),
                ('texto', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoInicial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activo', models.BooleanField(default=True)),
                ('tipo', models.CharField(max_length=30, choices=[(b'inicio', b'Inicio'), (b'distribucion', b'Distribucion'), (b'produccion', b'Produccion'), (b'postproduccion', b'Postproduccion'), (b'publicidad', b'Publicidad')])),
                ('codigo', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
