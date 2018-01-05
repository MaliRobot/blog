# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-05 22:32
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0002_auto_20180102_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('public', models.BooleanField()),
                ('language', models.CharField(default='eng', max_length=3)),
                ('image', models.ImageField(default=None, upload_to='flow/static/images/')),
                ('date_published', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'verbose_name_plural': 'news',
            },
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to='flow/static/images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
