# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0006_auto_20150516_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='num_stars',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detail',
            name='picture_path',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='regist_date',
            field=models.DateTimeField(verbose_name='date registered', default=datetime.datetime(2015, 5, 16, 4, 36, 44, 399537, tzinfo=utc)),
        ),
    ]
