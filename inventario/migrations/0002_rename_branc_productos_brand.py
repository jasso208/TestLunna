# Generated by Django 3.2.4 on 2021-06-24 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='branc',
            new_name='brand',
        ),
    ]