# Generated by Django 2.1 on 2019-10-26 21:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0014_auto_20190707_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 27, 2, 51, 14, 651524, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2293, 8, 10, 2, 51, 14, 651524, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 27, 2, 51, 14, 651524, tzinfo=utc), null=True),
        ),
    ]