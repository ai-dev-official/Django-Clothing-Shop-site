# Generated by Django 4.0.2 on 2022-04-14 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendors', '0015_remove_vendor_shop_name_vendor_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='bank_account_name',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='created_by',
        ),
        migrations.AddField(
            model_name='vendor',
            name='account_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to=settings.AUTH_USER_MODEL),
        ),
    ]
