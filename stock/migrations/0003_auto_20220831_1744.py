# Generated by Django 3.1.2 on 2022-08-31 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20220831_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='detalle',
            field=models.CharField(default=1, max_length=150, verbose_name='Observaciones'),
            preserve_default=False,
        ),
    ]
