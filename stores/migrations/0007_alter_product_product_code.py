# Generated by Django 4.1.2 on 2022-10-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0006_product_product_code_alter_product_battery_capacity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
