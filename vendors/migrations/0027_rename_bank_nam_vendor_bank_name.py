# Generated by Django 4.0.2 on 2022-04-25 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0026_rename_bank_name_vendor_bank_nam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='bank_nam',
            new_name='bank_name',
        ),
    ]
