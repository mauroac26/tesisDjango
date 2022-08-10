# Generated by Django 3.1.2 on 2022-08-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_ventas_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formapagoventa',
            name='tipoDebito',
        ),
        migrations.AddField(
            model_name='formapagoventa',
            name='tipoPago',
            field=models.IntegerField(choices=[[1, 'Efectivo'], [2, 'Credito'], [3, 'Debito']], default=1, verbose_name='Tipo Pago'),
            preserve_default=False,
        ),
    ]
