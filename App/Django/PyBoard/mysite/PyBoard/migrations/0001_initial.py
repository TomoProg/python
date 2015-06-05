# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('topic', models.CharField(max_length=512)),
                ('create_user', models.CharField(max_length=256)),
                ('create_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('del_flag', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TopicArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('article_no', models.IntegerField()),
                ('create_user', models.CharField(max_length=256)),
                ('article', models.TextField(blank=True)),
                ('create_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('del_flag', models.IntegerField(default=0)),
                ('topic_id', models.ForeignKey(to='PyBoard.Board')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('password', models.CharField(max_length=256)),
                ('create_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('del_flag', models.IntegerField(default=0)),
            ],
        ),
    ]
