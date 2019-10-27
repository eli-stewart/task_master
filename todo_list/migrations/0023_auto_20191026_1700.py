# Generated by Django 2.1 on 2019-10-27 00:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0022_auto_20191026_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 27, 5, 30, 51, 497787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2293, 8, 10, 5, 30, 51, 497787, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 27, 5, 30, 51, 497787, tzinfo=utc), null=True),
        ),
    ]