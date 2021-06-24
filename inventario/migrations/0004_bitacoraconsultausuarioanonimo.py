# Generated by Django 3.2.4 on 2021-06-24 20:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_productos_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='BitacoraConsultaUsuarioAnonimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime(2021, 6, 24, 20, 55, 30, 876237))),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.productos')),
            ],
        ),
    ]