# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_galeria_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado_proyecto',
            name='activo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
