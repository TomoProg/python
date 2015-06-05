# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0008_auto_20150519_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='regist_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 20, 40, 5, 849181, tzinfo=utc), verbose_name='date registered'),
        ),
    ]
