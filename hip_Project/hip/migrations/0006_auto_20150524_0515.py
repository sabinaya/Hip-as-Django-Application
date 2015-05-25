# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hip', '0005_auto_20150524_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='img1',
            field=models.CharField(default=b'0', max_length=1),
        ),
    ]
