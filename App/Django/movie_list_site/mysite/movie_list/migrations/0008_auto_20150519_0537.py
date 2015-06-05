# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0007_auto_20150516_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(to='movie_list.Genre', default=1),
        ),
        migrations.AddField(
            model_name='movie',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='num_stars',
            field=models.IntegerField(default=0, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='picture_path',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='regist_date',
            field=models.DateTimeField(verbose_name='date registered', default=datetime.datetime(2015, 5, 18, 20, 37, 46, 627810, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]
