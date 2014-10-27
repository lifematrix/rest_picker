# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('menu', models.CharField(max_length=100)),
                ('web', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=20)),
                ('picture', models.ImageField(null=True, upload_to=b'images/')),
                ('map', models.ImageField(null=True, upload_to=b'images/')),
                ('gmap_url', models.CharField(max_length=200, null=True)),
                ('votes', models.IntegerField(default=4, choices=[(1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five')])),
                ('food', models.ForeignKey(to='restaurants.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='town',
            field=models.ForeignKey(to='restaurants.Town'),
            preserve_default=True,
        ),
    ]
