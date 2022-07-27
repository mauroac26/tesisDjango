# Generated by Django 3.1.2 on 2022-06-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='tipoComprobante',
            field=models.CharField(choices=[['Factura', 'Factura'], ['Recibo', 'Recibo'], ['Nota Credito', 'Nota Credito']], max_length=150, verbose_name='Tipo Comprobante'),
        ),
    ]
