# Generated by Django 3.1.2 on 2022-08-04 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_compras_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='formaPagoCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Monto')),
                ('transferencia', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Transferencia')),
                ('cheques', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Cheques')),
                ('id_compra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.compras')),
            ],
        ),
    ]