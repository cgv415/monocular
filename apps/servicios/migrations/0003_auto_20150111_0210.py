# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_auto_20150111_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corto',
            name='trailer',
            field=models.SlugField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
