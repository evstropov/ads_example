# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='Hits', blank=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('author', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
                'verbose_name': 'ad',
                'verbose_name_plural': 'ads',
            },
        ),
        migrations.CreateModel(
            name='AdUserHit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('ad', models.ForeignKey(to='ads.Ad')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
