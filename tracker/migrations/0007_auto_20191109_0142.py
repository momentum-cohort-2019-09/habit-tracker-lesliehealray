# Generated by Django 2.2.7 on 2019-11-09 01:42

from django.db import migrations, models
from datetime import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20191108_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='log_date',
            field=models.DateTimeField(default=datetime.now()),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='log',
            name='log_detail',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='log',
            name='log_number_completed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9),
        ),
    ]