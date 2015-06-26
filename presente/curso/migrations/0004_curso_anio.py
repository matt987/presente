# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_curso_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='anio',
            field=models.IntegerField(default=2015),
            preserve_default=True,
        ),
    ]
