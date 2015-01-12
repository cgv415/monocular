# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_auto_20150112_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vimeo',
            name='codigo',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
