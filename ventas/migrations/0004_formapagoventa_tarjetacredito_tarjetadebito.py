# Generated by Django 3.1.2 on 2022-08-09 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20220421_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='tarjetaCredito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tarjetaDebito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='formaPagoVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Monto')),
                ('cuotas', models.IntegerField(blank=True, null=True)),
                ('id_venta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.ventas')),
                ('tipoCredito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ventas.tarjetacredito', verbose_name='Seleccionar Tarjeta')),
                ('tipoDebito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ventas.tarjetadebito')),
            ],
        ),
    ]