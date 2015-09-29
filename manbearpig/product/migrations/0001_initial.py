# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('lookupcode', models.IntegerField()),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('itemType', models.PositiveSmallIntegerField()),
                ('cost', models.DecimalField(max_digits=9, decimal_places=2)),
                ('quantity', models.IntegerField()),
                ('reorderPoint', models.IntegerField()),
                ('restockLevel', models.IntegerField()),
                ('extendedDescription', models.TextField()),
                ('active', models.BooleanField()),
                ('msrp', models.DecimalField(max_digits=9, decimal_places=2)),
                ('dateCreated', models.DateField(auto_now_add=True)),
                ('parentItem', models.ForeignKey(to='product.Product')),
            ],
        ),
    ]
