# Generated by Django 4.2.1 on 2023-06-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_productincart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productincart',
            name='quantity',
            field=models.PositiveIntegerField(max_length=100),
        ),
    ]