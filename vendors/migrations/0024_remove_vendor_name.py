# Generated by Django 4.0.2 on 2022-04-17 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0023_vendor_name_alter_vendor_county_alter_vendor_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='name',
        ),
    ]
