# Generated by Django 4.2.1 on 2023-05-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0023_trader_trader_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trader',
            name='trader_id',
        ),
        migrations.AlterField(
            model_name='trade',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
