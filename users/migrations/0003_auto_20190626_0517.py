# Generated by Django 2.2.2 on 2019-06-26 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190626_0454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='office',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
    ]