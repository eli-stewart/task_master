# Generated by Django 2.1 on 2019-10-26 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('creator', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('video', models.CharField(max_length=100)),
                ('metric', models.CharField(max_length=100)),
            ],
        ),
    ]