# Generated by Django 2.2.7 on 2019-11-09 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20191109_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='habit',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='log',
            name='log_date',
            field=models.DateField(),
        ),
    ]