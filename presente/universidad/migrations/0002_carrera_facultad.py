# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('universidad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='facultad',
            field=models.ForeignKey(to='universidad.Facultad', default=1),
            preserve_default=False,
        ),
    ]
