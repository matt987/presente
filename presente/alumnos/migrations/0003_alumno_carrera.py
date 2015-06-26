# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universidad', '0002_carrera_facultad'),
        ('alumnos', '0002_auto_20150327_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='carrera',
            field=models.ForeignKey(default=1, to='universidad.Carrera'),
            preserve_default=False,
        ),
    ]
