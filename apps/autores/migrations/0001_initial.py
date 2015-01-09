# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=200)),
                ('foto', models.ImageField(upload_to=b'foto_autor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
