# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 18:15
from __future__ import unicode_literals

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_commerce', '0004_auto_20161105_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'Euro')], default='XYZ', editable=False, max_length=3),
        ),
    ]
