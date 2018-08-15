# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20160122_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostlist',
            old_name='idc_jg',
            new_name='system',
        ),
    ]
