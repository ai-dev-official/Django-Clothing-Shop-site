# Generated by Django 4.0.2 on 2022-04-25 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_rename_vendor_product_vendo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='vendo',
            new_name='vendor',
        ),
    ]