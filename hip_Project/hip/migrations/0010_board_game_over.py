# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hip', '0009_auto_20150525_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='game_over',
            field=models.IntegerField(default=b'0', max_length=1),
            preserve_default=True,
        ),
    ]
