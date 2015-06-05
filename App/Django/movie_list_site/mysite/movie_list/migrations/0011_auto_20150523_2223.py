# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0010_auto_20150523_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='pic',
            field=models.ImageField(default='/home/tomoki/MyGitHub/python/App/Django/movie_list_site/mysite/static/media/default_image.png', upload_to='/home/tomoki/MyGitHub/python/App/Django/movie_list_site/mysite/static/media/upload'),
        ),
    ]
