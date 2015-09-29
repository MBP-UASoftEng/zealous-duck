# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zealousduck', '0004_auto_20150928_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='lookupcode',
            field=models.CharField(max_length=20),
        ),
    ]
