# Generated by Django 4.0.3 on 2022-03-24 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0007_alter_vendor_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='created_by',
            new_name='user',
        ),
    ]