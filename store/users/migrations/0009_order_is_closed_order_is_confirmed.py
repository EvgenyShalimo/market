# Generated by Django 4.2.1 on 2023-06-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_name_order_all_name_remove_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
