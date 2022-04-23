# Generated by Django 3.1.2 on 2021-11-25 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0003_auto_20211026_1853'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprobante', models.CharField(max_length=50, unique=True)),
                ('fecha', models.DateField()),
                ('tipoComprobante', models.IntegerField(choices=[[0, 'Factura'], [1, 'Recibo'], [2, 'Nota Credito']], verbose_name='Tipo Comprobante')),
                ('cuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
            ],
            options={
                'ordering': ('-fecha',),
            },
        ),
        migrations.CreateModel(
            name='detalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('iva', models.DecimalField(decimal_places=2, max_digits=8)),
                ('subTotal', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Sub-Total')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.ventas')),
            ],
        ),
    ]