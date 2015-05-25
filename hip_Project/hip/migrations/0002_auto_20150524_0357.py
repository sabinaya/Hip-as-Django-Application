# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='img1',
            field=models.CharField(default=b'0', max_length=1, editable=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='img2',
            field=models.CharField(default=b'0', max_length=1, editable=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='img3',
            field=models.CharField(default=b'0', max_length=1, editable=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='img4',
            field=models.CharField(default=b'0', max_length=1, editable=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='img5',
            field=models.CharField(default=b'0', max_length=1, editable=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='img6',
            field=models.CharField(default=b'0', max_length=1, editable=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='img7',
            field=models.CharField(default=b'0', max_length=1, editable=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='img8',
            field=models.CharField(default=b'0', max_length=1, editable=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='img9',
            field=models.CharField(default=b'0', max_length=1, editable=False),
        ),
    ]
