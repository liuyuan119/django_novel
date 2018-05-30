# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-29 14:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_title', models.CharField(max_length=255, verbose_name='标题')),
                ('a_info', models.CharField(max_length=300, verbose_name='简介')),
                ('a_content', models.TextField(verbose_name='内容')),
                ('a_img', models.ImageField(blank=True, null=True, upload_to='uploads', verbose_name='图片')),
                ('a_addtime', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('a_updatetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'art',
                'ordering': ['-a_addtime'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=255, verbose_name='标签名')),
                ('t_info', models.CharField(max_length=300, verbose_name='标签描述')),
                ('t_createtime', models.DateTimeField(db_index=True, default=datetime.datetime(2018, 5, 29, 14, 53, 25, 638949, tzinfo=utc))),
            ],
            options={
                'verbose_name': '标签',
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='art',
            name='a_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art.Tag'),
        ),
    ]
