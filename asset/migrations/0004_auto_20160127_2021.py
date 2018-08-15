# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20160122_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostlist',
            name='product',
            field=models.CharField(max_length=30, verbose_name='\u8bbe\u5907\u578b\u53f7'),
        ),
        migrations.AlterField(
            model_name='hostlist',
            name='system',
            field=models.CharField(max_length=30, verbose_name='\u64cd\u4f5c\u7cfb\u7edf', blank=True),
        ),
    ]
