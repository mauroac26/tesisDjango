# Generated by Django 3.1.2 on 2022-08-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20220820_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formapagoventa',
            name='tipoPago',
            field=models.CharField(choices=[['Efectivo', 'Efectivo'], ['Credito', 'Credito'], ['Debito', 'Debito']], max_length=150, verbose_name='Tipo Pago'),
        ),
    ]
