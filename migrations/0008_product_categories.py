# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 20:45
from __future__ import unicode_literals

from django.db import migrations
import wagtailcommerce.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=wagtailcommerce.fields.TreeManyToManyField(blank=True, null=True, to='wagtailcommerce.Category'),
        ),
    ]