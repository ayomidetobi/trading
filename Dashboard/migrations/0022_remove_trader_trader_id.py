# Generated by Django 4.2.1 on 2023-05-22 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0021_alter_trader_trader_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trader',
            name='trader_id',
        ),
    ]