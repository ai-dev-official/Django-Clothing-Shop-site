# Generated by Django 4.0.3 on 2022-04-22 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_orderitem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='color',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
