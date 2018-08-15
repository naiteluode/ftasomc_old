# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=20, verbose_name='IP\u5730\u5740')),
                ('hostname', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('product', models.CharField(max_length=20, verbose_name='\u4ea7\u54c1')),
                ('application', models.CharField(max_length=20, verbose_name='\u5e94\u7528')),
                ('idc_jg', models.CharField(max_length=10, verbose_name='\u673a\u67dc\u7f16\u53f7', blank=True)),
                ('status', models.CharField(max_length=10, verbose_name='\u4f7f\u7528\u72b6\u6001')),
                ('remark', models.TextField(max_length=50, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u5217\u8868\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='IdcAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idc_name', models.CharField(max_length=20, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('idc_type', models.CharField(max_length=20, verbose_name='\u673a\u623f\u7c7b\u578b')),
                ('idc_location', models.CharField(max_length=30, verbose_name='\u673a\u623f\u4f4d\u7f6e')),
                ('contract_date', models.CharField(max_length=30, verbose_name='\u5408\u540c\u65f6\u95f4')),
                ('idc_contacts', models.CharField(max_length=30, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('remark', models.TextField(default=b'', max_length=50, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': 'IDC\u8d44\u4ea7\u4fe1\u606f',
                'verbose_name_plural': 'IDC\u8d44\u4ea7\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='NetworkAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=20, verbose_name='IP\u5730\u5740')),
                ('hostname', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='\u5382\u5546')),
                ('productname', models.CharField(max_length=20, verbose_name='\u4ea7\u54c1\u578b\u53f7')),
                ('idc_jg', models.CharField(max_length=10, verbose_name='\u673a\u67dc\u7f16\u53f7', blank=True)),
                ('service_tag', models.CharField(unique=True, max_length=30, verbose_name='\u5e8f\u5217\u53f7')),
                ('remark', models.TextField(default=b'', max_length=50, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u7f51\u7edc\u8bbe\u5907\u8d44\u4ea7\u4fe1\u606f',
                'verbose_name_plural': '\u7f51\u7edc\u8bbe\u5907\u8d44\u4ea7\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='ServerAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manufacturer', models.CharField(max_length=20, verbose_name='\u5382\u5546')),
                ('productname', models.CharField(max_length=30, verbose_name='\u4ea7\u54c1\u578b\u53f7')),
                ('service_tag', models.CharField(unique=True, max_length=80, verbose_name='\u5e8f\u5217\u53f7')),
                ('cpu_model', models.CharField(max_length=50, verbose_name='CPU\u578b\u53f7')),
                ('cpu_nums', models.PositiveSmallIntegerField(verbose_name='CPU\u7ebf\u7a0b\u6570')),
                ('cpu_groups', models.PositiveSmallIntegerField(verbose_name='CPU\u7269\u7406\u6838\u6570')),
                ('mem', models.CharField(max_length=5, verbose_name=b'\xe5\x86\x85\xe5\xad\x98\xe5\xa4\xa7\xe5\xb0\x8f')),
                ('disk', models.CharField(max_length=5, verbose_name=b'\xe7\xa1\xac\xe7\x9b\x98\xe5\xa4\xa7\xe5\xb0\x8f')),
                ('raid', models.CharField(max_length=5, verbose_name=b'RAID\xe7\xba\xa7\xe5\x88\xab')),
                ('hostname', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.CharField(max_length=20, verbose_name='IP\u5730\u5740')),
                ('macaddress', models.CharField(max_length=40, verbose_name='MAC\u5730\u5740')),
                ('os', models.CharField(max_length=20, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('virtual', models.CharField(max_length=20, verbose_name='\u662f\u5426\u4e3a\u865a\u62df\u673a')),
                ('idc_name', models.CharField(max_length=10, verbose_name='\u6240\u5c5e\u673a\u623f', blank=True)),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u8d44\u4ea7\u4fe1\u606f',
                'verbose_name_plural': '\u4e3b\u673a\u8d44\u4ea7\u4fe1\u606f\u7ba1\u7406',
            },
        ),
    ]
