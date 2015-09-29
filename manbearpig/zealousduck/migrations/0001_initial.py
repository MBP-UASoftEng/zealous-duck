# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_first', models.CharField(max_length=100)),
                ('name_last', models.CharField(max_length=100)),
                ('active', models.BooleanField()),
                ('type', models.PositiveSmallIntegerField()),
                ('password', models.CharField(max_length=100)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('lookupcode', models.IntegerField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('itemType', models.PositiveSmallIntegerField()),
                ('cost', models.DecimalField(max_digits=10, decimal_places=2)),
                ('quantity', models.IntegerField()),
                ('reorderPoint', models.IntegerField()),
                ('restockLevel', models.IntegerField()),
                ('extendedDescription', models.TextField()),
                ('active', models.BooleanField()),
                ('msrp', models.DecimalField(max_digits=10, decimal_places=2)),
                ('dateCreated', models.DateField(auto_now_add=True)),
                ('parentItem', models.ForeignKey(to='zealousduck.Product')),
            ],
        ),
        migrations.CreateModel(
            name='TenderEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tenderType', models.PositiveSmallIntegerField()),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('transactionType', models.PositiveSmallIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cashierID', models.ForeignKey(to='zealousduck.Employee')),
                ('parent', models.ForeignKey(to='zealousduck.Transaction')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('quantity', models.IntegerField()),
                ('productID', models.ForeignKey(to='zealousduck.Product')),
                ('transactionID', models.ForeignKey(to='zealousduck.Transaction')),
            ],
        ),
        migrations.AddField(
            model_name='tenderentry',
            name='transactionID',
            field=models.ForeignKey(to='zealousduck.Transaction'),
        ),
    ]
