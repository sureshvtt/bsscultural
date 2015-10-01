# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('affiliation_no', models.CharField(unique=True, max_length=25)),
                ('from_date', models.DateField(null=True, blank=True)),
                ('to_date', models.DateField(null=True, blank=True)),
                ('address', models.CharField(max_length=1024, null=True, blank=True)),
                ('mobile', models.CharField(max_length=100, null=True, blank=True)),
                ('Landphone', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution_Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='course.Course')),
                ('institution', models.ForeignKey(to='institution.Institution')),
            ],
        ),
    ]
