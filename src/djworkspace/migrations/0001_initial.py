# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 00:32
from __future__ import unicode_literals

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40)),
                ('key', models.CharField(max_length=40)),
                ('results', picklefield.fields.PickledObjectField(editable=False)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='cache',
            unique_together=set([('type', 'key')]),
        ),
    ]
