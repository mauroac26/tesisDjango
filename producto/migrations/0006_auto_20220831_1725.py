# Generated by Django 3.1.2 on 2022-08-31 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_delete_prueba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock_min',
            field=models.IntegerField(verbose_name='Stock Minimo'),
        ),
    ]