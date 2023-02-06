# Generated by Django 4.1.2 on 2022-10-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0012_alter_product_battery_capacity_alter_product_brand_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_code',
        ),
        migrations.AlterField(
            model_name='product',
            name='battery_capacity',
            field=models.CharField(default='No deatil', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='No deatil', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='camera',
            field=models.CharField(default='No deatil', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='network',
            field=models.CharField(default='No deatil', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='os',
            field=models.CharField(default='No deatil', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.CharField(default='No deatil', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='screen_size',
            field=models.CharField(default='No deatil', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='sim_slot',
            field=models.CharField(default='No deatil', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='sim_type',
            field=models.CharField(default='No deatil', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.CharField(default='No deatil', max_length=100),
        ),
    ]