# Generated by Django 4.0.3 on 2022-04-11 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_paid_amount_alter_order_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid_amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='place',
        ),
    ]
