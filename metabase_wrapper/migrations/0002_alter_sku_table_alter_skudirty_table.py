# Generated by Django 4.1.2 on 2022-10-25 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metabase_wrapper', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='sku',
            table='sku',
        ),
        migrations.AlterModelTable(
            name='skudirty',
            table='sku_dirty',
        ),
    ]
