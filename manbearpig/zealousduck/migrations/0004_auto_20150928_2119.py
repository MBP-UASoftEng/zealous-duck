# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zealousduck', '0003_auto_20150928_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='parentItem',
        ),
        migrations.AddField(
            model_name='product',
            name='itemID',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='parentID',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
