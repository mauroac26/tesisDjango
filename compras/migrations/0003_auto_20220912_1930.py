# Generated by Django 3.1.2 on 2022-09-12 19:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proveedores', '0002_auto_20211026_1852'),
        ('compras', '0002_auto_20220820_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 9, 12, 19, 30, 33, 135569), verbose_name='Fecha de Creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compras',
            name='deleted_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Eliminación'),
        ),
        migrations.AddField(
            model_name='compras',
            name='modified_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Modificación'),
        ),
        migrations.AlterField(
            model_name='compras',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='HistoricalCompras',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('comprobante', models.CharField(db_index=True, max_length=50)),
                ('fecha', models.DateField()),
                ('tipoComprobante', models.CharField(choices=[['Factura', 'Factura'], ['Recibo', 'Recibo'], ['Nota Credito', 'Nota Credito']], max_length=150, verbose_name='Tipo Comprobante')),
                ('estado', models.CharField(default='Adeudado', max_length=150)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('cuit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='proveedores.proveedores')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical compras',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
