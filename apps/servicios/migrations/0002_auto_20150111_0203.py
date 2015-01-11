# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corto',
            name='trailer',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
