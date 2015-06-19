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
            name='Planilla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('materia', models.ForeignKey(to='universidad.Materia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanillaPorAlumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asistencia', models.BooleanField(default=True)),
                ('alumno', models.ForeignKey(to='alumnos.Alumno')),
                ('planilla', models.ForeignKey(to='Planilla.Planilla')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
