# Generated by Django 2.0.9 on 2018-12-12 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_auto_20181212_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='perm',
            field=models.BooleanField(default=True, verbose_name='Permission Granted'),
        ),
        migrations.AlterField(
            model_name='request',
            name='time',
            field=models.TimeField(default=datetime.time(14, 42, 31, 612078), null=True, verbose_name='Time'),
        ),
    ]
