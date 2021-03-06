# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activo', models.BooleanField(default=True)),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('resumen', models.TextField()),
                ('imagen', models.ImageField(upload_to=b'noticias')),
                ('fecha', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
