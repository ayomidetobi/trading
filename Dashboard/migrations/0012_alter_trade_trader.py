# Generated by Django 4.2.1 on 2023-05-21 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0011_alter_trade_trader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='trader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
