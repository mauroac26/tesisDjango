# Generated by Django 3.1.2 on 2021-05-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_detallecompra_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compras',
            name='iva',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='subTotal',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='total',
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='subTotal',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=8, verbose_name='Sub-Total'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='compras',
            name='comprobante',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='compras',
            name='tipoComprobante',
            field=models.IntegerField(choices=[[0, 'Factura'], [1, 'Recibo'], [2, 'Nota Credito']], verbose_name='Tipo Comprobante'),
        ),
    ]