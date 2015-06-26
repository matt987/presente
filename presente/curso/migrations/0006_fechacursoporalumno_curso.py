# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0005_auto_20150626_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='fechacursoporalumno',
            name='curso',
            field=models.ForeignKey(default=1, to='curso.Curso'),
            preserve_default=False,
        ),
    ]
