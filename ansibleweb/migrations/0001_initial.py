# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.TextField()),
                ('cmd', models.TextField()),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('rc', models.IntegerField(null=True)),
                ('stdout', models.TextField(null=True)),
                ('stderr', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inventory', models.TextField()),
                ('sudo', models.BooleanField(default=True)),
                ('cmd', models.TextField()),
                ('rc', models.IntegerField(null=True)),
                ('farmer', models.TextField()),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='task',
            field=models.ForeignKey(to='ansibleweb.Task'),
        ),
    ]
