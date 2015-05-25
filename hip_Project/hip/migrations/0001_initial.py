# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img1', models.CharField(max_length=1)),
                ('img2', models.CharField(max_length=1)),
                ('img3', models.CharField(max_length=1)),
                ('img4', models.CharField(max_length=1)),
                ('img5', models.CharField(max_length=1)),
                ('img6', models.CharField(max_length=1)),
                ('img7', models.CharField(max_length=1)),
                ('img8', models.CharField(max_length=1)),
                ('img9', models.CharField(max_length=1)),
                ('Player', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
