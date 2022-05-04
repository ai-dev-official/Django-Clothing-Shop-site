# Generated by Django 4.0.2 on 2022-02-26 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('default', models.BooleanField(default=False)),
                ('width', models.FloatField(default=300)),
                ('length', models.FloatField(default=300)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product')),
            ],
        ),
    ]