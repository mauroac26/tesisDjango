# Generated by Django 3.1.2 on 2022-08-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_auto_20220804_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='formapagocompra',
            name='fecha',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formapagocompra',
            name='tipoPago',
            field=models.CharField(choices=[['Efectivo', 'Efectivo'], ['Transferencia', 'Transferencia'], ['Cheques', 'Cheques']], max_length=150, verbose_name='Tipo Pago'),
        ),
    ]
