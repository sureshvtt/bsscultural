# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marklist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mark', models.IntegerField()),
                ('exam_no', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('reg_no', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10, null=True, blank=True)),
                ('age', models.CharField(max_length=5, null=True, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('guardian_name', models.CharField(max_length=1024, null=True, blank=True)),
                ('duration', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=1024, null=True, blank=True)),
                ('mobile', models.CharField(max_length=15, null=True, blank=True)),
                ('Landphone', models.CharField(max_length=15, null=True, blank=True)),
                ('marklist_status', models.BooleanField()),
                ('certificate_status', models.BooleanField()),
                ('course', models.ForeignKey(to='course.Course')),
                ('institution', models.ForeignKey(to='institution.Institution')),
            ],
        ),
        migrations.AddField(
            model_name='marklist',
            name='student',
            field=models.ForeignKey(to='student.Student'),
        ),
        migrations.AddField(
            model_name='marklist',
            name='subject',
            field=models.ForeignKey(to='course.Subject'),
        ),
    ]
