# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0009_auto_20150519_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='picture_path',
        ),
        migrations.AddField(
            model_name='movie',
            name='pic',
            field=models.ImageField(upload_to='/home/tomoki/MyGitHub/python/App/Django/movie_list_site/mysite/static/media', default='/home/tomoki/MyGitHub/python/App/Django/movie_list_site/mysite/static/media/default_image.png'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='regist_date',
            field=models.DateTimeField(verbose_name='date registered', default=django.utils.timezone.now),
        ),
    ]
