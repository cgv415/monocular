# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='servicio',
            field=models.ManyToManyField(to='servicios.Servicio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicioproyecto',
            name='servicio',
            field=models.ForeignKey(to='servicios.Servicio'),
            preserve_default=True,
        ),
    ]
