# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zealousduck', '0009_auto_20150929_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.DecimalField(default=b'0.00', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='itemType',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Normal'), (b'1', b'Serialized'), (b'2', b'Matrix')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='msrp',
            field=models.DecimalField(default=b'0.00', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='parentID',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=b'0.00', max_digits=10, decimal_places=2),
        ),
    ]
