# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_remove_curso_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='descripcion',
            field=models.CharField(max_length=200, default=''),
        ),
    ]
