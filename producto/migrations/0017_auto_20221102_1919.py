# Generated by Django 3.1.2 on 2022-11-02 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0016_auto_20221019_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproductopromocion',
            name='id_producto',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='producto.producto', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='productopromocion',
            name='id_producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.producto', verbose_name='Producto'),
        ),
    ]
