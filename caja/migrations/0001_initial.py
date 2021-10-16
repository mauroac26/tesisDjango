# Generated by Django 3.1.2 on 2021-10-15 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('descripcion', models.CharField(max_length=50)),
                ('operacion', models.IntegerField(choices=[[0, 'Ingreso'], [1, 'Egreso']], default=0)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
