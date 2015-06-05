# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie_list', '0002_auto_20150516_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('genre', models.ForeignKey(to='movie_list.Genre')),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='regist_date',
            field=models.DateTimeField(default=timezone.now(), verbose_name='date registered'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='movie',
            field=models.ForeignKey(to='movie_list.Movie'),
        ),
    ]
