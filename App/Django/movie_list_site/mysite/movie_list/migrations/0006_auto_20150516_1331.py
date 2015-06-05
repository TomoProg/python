# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0005_auto_20150516_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='regist_date',
            field=models.DateTimeField(verbose_name='date registered', default=datetime.datetime(2015, 5, 16, 4, 31, 42, 575163, tzinfo=utc)),
        ),
    ]
