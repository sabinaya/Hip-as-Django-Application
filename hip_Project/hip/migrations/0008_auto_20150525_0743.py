# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hip', '0007_auto_20150525_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='img1',
            field=models.IntegerField(max_length=9),
        ),
    ]
