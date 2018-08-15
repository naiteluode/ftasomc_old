# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ansibleweb', '0002_task_use'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='use',
            field=models.DateTimeField(null=True),
        ),
    ]
