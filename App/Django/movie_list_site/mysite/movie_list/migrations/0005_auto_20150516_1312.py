# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0004_auto_20150516_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='note',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='num_stars',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='picture_path',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='regist_date',
            field=models.DateTimeField(verbose_name='date registered', default=datetime.datetime(2015, 5, 16, 4, 12, 26, 312169, tzinfo=utc)),
        ),
    ]
