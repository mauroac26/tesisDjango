# Generated by Django 3.2.14 on 2022-07-27 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0004_rename_caja_movcaja'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='movcaja',
            name='id_caja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='caja.caja'),
            preserve_default=False,
        ),
    ]