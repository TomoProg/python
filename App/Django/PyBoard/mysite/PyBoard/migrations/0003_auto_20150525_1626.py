# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PyBoard', '0002_auto_20150525_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicarticle',
            name='create_user',
            field=models.ForeignKey(to='PyBoard.UserInfo'),
        ),
    ]
