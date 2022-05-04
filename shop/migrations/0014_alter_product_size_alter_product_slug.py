# Generated by Django 4.0.3 on 2022-04-13 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_remove_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('S', 'S'), ('XS', 'XS')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=255),
        ),
    ]
