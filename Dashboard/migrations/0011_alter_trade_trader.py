# Generated by Django 4.2.1 on 2023-05-21 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0010_alter_trade_trader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='trader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.trader'),
        ),
    ]
