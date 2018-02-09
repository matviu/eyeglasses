# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eyeglasses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show', models.BooleanField(default=True, verbose_name='Show on site')),
                ('last_modified', models.DateTimeField(default=datetime.datetime(2018, 1, 16, 16, 46, 22, 800000, tzinfo=utc), verbose_name='Datetime last modified', auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(max_length=200, verbose_name='\u0441\u043b\u0430\u0433')),
                ('description', models.TextField(max_length=500, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('price', models.DecimalField(verbose_name='\u0446\u0435\u043d\u0430', max_digits=8, decimal_places=2, blank=True)),
                ('discount', models.PositiveSmallIntegerField(default=0, blank=True, verbose_name='\u0441\u043a\u0438\u0434\u043a\u0430(\u0432 \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u0430\u0445)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('rating', models.PositiveSmallIntegerField(default=5, blank=True, verbose_name='\u0440\u0435\u0439\u0442\u0438\u043d\u0433', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('type', models.CharField(blank=True, max_length=50, choices=[('1', '\u0442\u043e\u043d\u043a\u043e\u0435 \u0441\u0442\u0435\u043a\u043b\u043e'), ('2', '\u0441\u0440\u0435\u0434\u043d\u0435\u0435 \u0441\u0442\u0435\u043a\u043b\u043e'), ('3', '\u0442\u043e\u043b\u0441\u0442\u043e\u0435 \u0441\u0442\u0435\u043a\u043b\u043e')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show', models.BooleanField(default=True, verbose_name='Show on site')),
                ('last_modified', models.DateTimeField(default=datetime.datetime(2018, 1, 16, 16, 46, 22, 800000, tzinfo=utc), verbose_name='Datetime last modified', auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(max_length=200, verbose_name='\u0441\u043b\u0430\u0433')),
                ('description', models.TextField(max_length=500, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('add_description', models.TextField(max_length=500, verbose_name='\u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
