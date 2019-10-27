# Generated by Django 2.1 on 2019-10-26 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('metric', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='asend.Category'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='creator',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='entries',
            field=models.ManyToManyField(related_name='entries', to='asend.Entry'),
        ),
    ]