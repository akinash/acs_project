# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acs_app', '0003_auto_20170414_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passtypes',
            name='pass_type',
            field=models.CharField(choices=[('enter', 'Вход'), ('exit', 'Выход')], max_length=5, null=True),
        ),
    ]
