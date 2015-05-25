# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hip', '0006_auto_20150524_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='Player',
        ),
        migrations.RemoveField(
            model_name='board',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='board',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='board',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='board',
            name='img5',
        ),
        migrations.RemoveField(
            model_name='board',
            name='img6',
        ),
        migrations.RemoveField(
            model_name='board',
            name='img7',
        ),
        migrations.RemoveField(
            model_name='board',
            name='img8',
        ),
        migrations.RemoveField(
            model_name='board',
            name='img9',
        ),
        migrations.AddField(
            model_name='board',
            name='player',
            field=models.CharField(default=b'none', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='board',
            name='img1',
            field=models.IntegerField(max_length=1),
        ),
    ]
