# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zealousduck', '0007_auto_20150928_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='extendedDescription',
            field=models.TextField(blank=True),
        ),
    ]
