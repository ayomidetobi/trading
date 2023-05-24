# Generated by Django 4.1.9 on 2023-05-22 10:27

import Dashboard.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0007_alter_trade_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trade',
            name='profit_loss',
            field=models.DecimalField(decimal_places=2, default=Dashboard.models.generate_random_float, max_digits=10),
        ),
        migrations.AlterField(
            model_name='trade',
            name='trader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]