# Generated by Django 4.0.2 on 2022-04-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_product_size_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('Yellow', 'Yellow'), ('Red', 'Red'), ('Green', 'Green'), ('Orange', 'Orange'), ('Black', 'Black')], default='Yellow', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('S', 'S'), ('XS', 'XS')], default='M', max_length=6, null=True),
        ),
    ]