# Generated by Django 3.1.2 on 2022-12-18 09:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('caja', '0006_caja_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caja',
            options={'verbose_name': 'Modelo Base', 'verbose_name_plural': 'Modelos Base'},
        ),
        migrations.AlterModelOptions(
            name='movcaja',
            options={'verbose_name': 'Modelo Base', 'verbose_name_plural': 'Modelos Base'},
        ),
        migrations.AddField(
            model_name='caja',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 12, 18, 9, 59, 1, 558944), verbose_name='Fecha de Creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caja',
            name='deleted_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Eliminación'),
        ),
        migrations.AddField(
            model_name='caja',
            name='modified_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Modificación'),
        ),
        migrations.AddField(
            model_name='movcaja',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 12, 18, 9, 59, 11, 233172), verbose_name='Fecha de Creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movcaja',
            name='deleted_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Eliminación'),
        ),
        migrations.AddField(
            model_name='movcaja',
            name='modified_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Modificación'),
        ),
        migrations.AlterField(
            model_name='caja',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movcaja',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='HistoricalmovCaja',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('fecha', models.DateTimeField()),
                ('descripcion', models.CharField(max_length=50)),
                ('operacion', models.IntegerField(choices=[[0, 'Ingreso'], [1, 'Egreso']], default=0)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('id_caja', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='caja.caja')),
            ],
            options={
                'verbose_name': 'historical Modelo Base',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCaja',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=50)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('estado', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Modelo Base',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]