# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zealousduck', '0005_auto_20150928_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='lookupcode',
            field=models.CharField(max_length=30),
        ),
    ]
