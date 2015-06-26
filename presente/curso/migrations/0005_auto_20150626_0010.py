# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0004_curso_anio'),
    ]

    operations = [
        migrations.CreateModel(
            name='FechaCursoPorAlumno',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fecha', models.DateField()),
                ('asistencia', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('curso_por_alumno', models.ForeignKey(to='curso.CursoPorAlumno')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cursoporalumno',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2015, 6, 26, 0, 10, 22, 668983, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cursoporalumno',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2015, 6, 26, 0, 10, 36, 184856, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
