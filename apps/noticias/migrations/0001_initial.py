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
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('imagen', models.ImageField(upload_to=b'noticias')),
                ('resumen', models.TextField()),
                ('fecha', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
