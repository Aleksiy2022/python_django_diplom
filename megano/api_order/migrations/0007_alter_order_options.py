# Generated by Django 4.2.2 on 2023-09-12 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_order', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-createdAt'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]