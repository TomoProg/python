# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='書籍名')),
                ('publisher', models.CharField(blank=True, verbose_name='出版社', max_length=255)),
                ('page', models.IntegerField(blank=True, verbose_name='ページ数', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('comment', models.TextField(blank=True, verbose_name='コメント')),
                ('book', models.ForeignKey(to='cms.Book', verbose_name='書籍', related_name='impressions')),
            ],
        ),
    ]
