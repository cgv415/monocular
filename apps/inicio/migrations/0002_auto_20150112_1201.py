# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vimeo',
            name='codigo',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
