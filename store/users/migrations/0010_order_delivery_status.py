# Generated by Django 4.2.1 on 2023-07-15 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_order_is_closed_order_is_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(choices=[('pending', 'Ожидает доставки'), ('in_transit', 'В пути'), ('delivered', 'Доставлен')], default='pending', max_length=20),
        ),
    ]