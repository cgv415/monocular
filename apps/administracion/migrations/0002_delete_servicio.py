# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_auto_20150116_1052'),
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Servicio',
        ),
    ]
