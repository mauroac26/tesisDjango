# Generated by Django 3.1.2 on 2022-07-26 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='id_compra',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
