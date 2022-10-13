# Generated by Django 3.1.2 on 2022-09-30 19:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0014_auto_20220922_1739'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produccion', '0004_auto_20220930_1925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produccion',
            options={'verbose_name': 'Modelo Base', 'verbose_name_plural': 'Modelos Base'},
        ),
        migrations.AddField(
            model_name='produccion',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 9, 30, 19, 26, 55, 855250), verbose_name='Fecha de Creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produccion',
            name='deleted_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Eliminación'),
        ),
        migrations.AddField(
            model_name='produccion',
            name='modified_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Modificación'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='HistoricalProduccion',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('fecha', models.DateField()),
                ('cantidad_retiro', models.IntegerField(default=1, verbose_name='Cantidad  Retiro')),
                ('cantidad_pedido', models.IntegerField(default=1, verbose_name='Cantidad Pedido')),
                ('estado', models.CharField(choices=[['Pendiente', 'Pendiente'], ['Producido', 'Producido']], default='Pendiente', max_length=50, verbose_name='Estado')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('producto_pedido', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='producto.producto')),
                ('producto_retiro', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='producto.producto')),
                ('usuario', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Modelo Base',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]