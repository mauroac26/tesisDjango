# Generated by Django 3.1.2 on 2022-11-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_auto_20211026_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='cuit',
            field=models.CharField(max_length=13, primary_key=True, serialize=False, unique=True),
        ),
    ]
