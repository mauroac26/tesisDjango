# Generated by Django 3.1.2 on 2022-08-19 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0020_delete_prueba'),
    ]

    operations = [
        migrations.AddField(
            model_name='formapagocompra',
            name='fecha',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
