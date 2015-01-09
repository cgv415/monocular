# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corto',
            name='palmares',
        ),
        migrations.AlterField(
            model_name='corto',
            name='anyo',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='corto',
            name='duracion',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='corto',
            name='trailer',
            field=models.CharField(max_length=150, null=True),
            preserve_default=True,
        ),
    ]
