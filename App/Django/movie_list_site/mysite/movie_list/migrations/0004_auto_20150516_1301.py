# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0003_auto_20150516_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='regist_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 4, 1, 22, 670448, tzinfo=utc), verbose_name='date registered'),
        ),
    ]
