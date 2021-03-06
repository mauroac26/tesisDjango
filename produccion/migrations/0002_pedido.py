# Generated by Django 3.1.2 on 2022-05-10 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_auto_20211026_1853'),
        ('produccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('estado', models.CharField(choices=[['Pendiente', 'Pendiente'], ['Producido', 'Producido']], max_length=50, verbose_name='Estado')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
            ],
        ),
    ]
