# Generated by Django 4.2.1 on 2023-05-19 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_order_user_alter_shippingaddress_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='user',
        ),
    ]
