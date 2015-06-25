# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_auto_20150327_1913'),
        ('universidad', '0002_carrera_facultad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fecha', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('materia', models.ForeignKey(to='universidad.Materia')),
            ],
        ),
        migrations.CreateModel(
            name='CursoPorAlumno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('alumno', models.ForeignKey(to='alumnos.Alumno')),
                ('curso', models.ForeignKey(to='curso.Curso')),
            ],
        ),
    ]
