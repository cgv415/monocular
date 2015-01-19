# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeria',
            name='titulo',
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='portfolio',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
