# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 14:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='repetable_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Tytu\u0142 wydarzenia', max_length=100, verbose_name='Tytu\u0142')),
                ('desc', models.TextField(blank=True, default='Opis wydarzenia', max_length=500, null=True, verbose_name='Opis')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Czas')),
                ('place', models.CharField(default='Tytu\u0142 wydarzenia', max_length=100, verbose_name='Miejsce')),
                ('time_begin', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Pocz\u0105tek')),
                ('time_end', models.DateTimeField(default=datetime.timedelta(0, 3600), verbose_name='Koniec')),
                ('date_begin', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Pocz\u0105tek')),
                ('date_end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Koniec')),
                ('offset', models.IntegerField(default=datetime.timedelta(1), verbose_name='Co ile dni')),
            ],
        ),
        migrations.CreateModel(
            name='single_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Tytu\u0142 wydarzenia', max_length=100, verbose_name='Tytu\u0142')),
                ('desc', models.TextField(blank=True, default='Opis wydarzenia', max_length=500, null=True, verbose_name='Opis')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Czas')),
                ('place', models.CharField(default='Tytu\u0142 wydarzenia', max_length=100, verbose_name='Miejsce')),
                ('begin', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Pocz\u0105tek')),
                ('end', models.DateTimeField(blank=True, default=datetime.timedelta(0, 3600), null=True, verbose_name='Koniec')),
            ],
        ),
    ]