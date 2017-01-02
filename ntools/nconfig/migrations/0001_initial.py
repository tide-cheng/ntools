# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename_text', models.CharField(max_length=200, unique=True, verbose_name='文件名')),
                ('fileadd_date', models.DateTimeField(auto_now_add=True, verbose_name='文件加入数据库时间')),
                ('file_file', models.FileField(upload_to='uploads/', verbose_name='文件位置')),
            ],
        ),
    ]
