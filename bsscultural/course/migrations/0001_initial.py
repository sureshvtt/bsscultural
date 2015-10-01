# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temp_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=1024)),
                ('duration', models.CharField(max_length=10)),
                ('eligibility', models.CharField(max_length=50, null=True, blank=True)),
                ('total_fee', models.CharField(max_length=10, null=True, blank=True)),
                ('Reg_fee', models.CharField(max_length=10, null=True, blank=True)),
                ('exam_fee', models.CharField(max_length=10, null=True, blank=True)),
                ('no_of_exams', models.CharField(max_length=10)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paper', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('max_mark', models.IntegerField()),
                ('min_mark', models.IntegerField()),
                ('is_theory', models.BooleanField()),
                ('course', models.ForeignKey(to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Subject_Heading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exam_no', models.CharField(max_length=10)),
                ('heading', models.CharField(max_length=200)),
                ('course', models.ForeignKey(to='course.Course')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='heading',
            field=models.ForeignKey(to='course.Subject_Heading'),
        ),
        migrations.AddField(
            model_name='paper',
            name='subject',
            field=models.ForeignKey(to='course.Subject'),
        ),
    ]
