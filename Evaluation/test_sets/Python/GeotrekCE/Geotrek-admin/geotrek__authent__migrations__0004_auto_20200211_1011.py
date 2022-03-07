# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-11 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import geotrek.authent.models


class Migration(migrations.Migration):

    dependencies = [
        ('authent', '0003_auto_20181203_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='structure',
            field=models.ForeignKey(default=geotrek.authent.models.default_structure_pk, on_delete=django.db.models.deletion.CASCADE, to='authent.Structure', verbose_name='Related structure'),
        ),
    ]