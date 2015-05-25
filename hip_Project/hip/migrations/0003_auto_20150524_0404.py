# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hip', '0002_auto_20150524_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='Player',
            field=models.CharField(default=b'none', max_length=10),
        ),
    ]
