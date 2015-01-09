# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ciudad', models.CharField(max_length=50)),
                ('servicio_Contratado', models.CharField(max_length=50, choices=[(b'cortometraje', b'Cortometraje'), (b'publicidad', b'Publicidad'), (b'etanolaje', b'Etanolaje'), (b'videoclip', b'Videoclip'), (b'otro', b'Otro')])),
                ('proyecto', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
