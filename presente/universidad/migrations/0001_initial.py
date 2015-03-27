# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=200)),
                ('telefono_administracion', models.CharField(max_length=200)),
                ('telefono_alumnado', models.CharField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('coordinador', models.ForeignKey(to='empleados.CoordinadorCarrera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono_administracion', models.CharField(max_length=200)),
                ('telefono_alumnado', models.CharField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('decano', models.ForeignKey(to='empleados.Decano')),
                ('recepcionista', models.ForeignKey(to='empleados.Recepcionista')),
                ('secretario', models.ForeignKey(to='empleados.Secretario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('profesor_titular', models.ForeignKey(to='empleados.Profesor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('carrera', models.ForeignKey(to='universidad.Carrera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='materia',
            name='semestre',
            field=models.ForeignKey(to='universidad.Semestre'),
            preserve_default=True,
        ),
    ]
