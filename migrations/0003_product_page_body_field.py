# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 09:15
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks
import wagtailcommerce.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce', '0002_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('alignment', wagtailcommerce.blocks.ImageFormatChoiceBlock()), ('caption', wagtail.wagtailcore.blocks.CharBlock()), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))), icon='image', label='Aligned image')), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')))),            
            preserve_default=False,
        ),
    ]