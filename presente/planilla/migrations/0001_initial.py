# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_remove_curso_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planilla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('curso', models.ForeignKey(to='curso.CursoPorAlumno')),
            ],
        ),
    ]
