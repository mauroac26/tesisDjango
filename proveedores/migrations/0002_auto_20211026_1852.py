# Generated by Django 3.1.2 on 2021-10-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='cuit',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, unique=True),
        ),
    ]
