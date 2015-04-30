# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('description', models.TextField()),
                ('engine', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('make', models.CharField(max_length=20)),
                ('owner', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
