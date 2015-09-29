# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zealousduck', '0006_auto_20150928_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='itemType',
            field=models.CharField(default=0, max_length=1, choices=[(b'0', b'Normal'), (b'1', b'Serialized'), (b'2', b'Matrix')]),
        ),
    ]
