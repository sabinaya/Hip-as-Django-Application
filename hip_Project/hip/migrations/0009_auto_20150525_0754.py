# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hip', '0008_auto_20150525_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='img2',
            field=models.IntegerField(default=b'0', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='board',
            name='img3',
            field=models.IntegerField(default=b'0', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='board',
            name='img4',
            field=models.IntegerField(default=b'0', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='board',
            name='img5',
            field=models.IntegerField(default=b'0', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='board',
            name='img6',
            field=models.IntegerField(default=b'0', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='board',
            name='img7',
            field=models.IntegerField(default=b'0', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='board',
            name='img8',
            field=models.IntegerField(default=b'0', max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='board',
            name='img9',
            field=models.IntegerField(default=b'0', max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='board',
            name='img1',
            field=models.IntegerField(default=b'0', max_length=1),
        ),
    ]
