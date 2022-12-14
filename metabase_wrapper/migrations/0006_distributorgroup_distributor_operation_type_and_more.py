# Generated by Django 4.1.3 on 2022-11-06 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metabase_wrapper', '0005_distributor_sofile_alter_sku_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistributorGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Группа Дистрибьюторов',
                'verbose_name_plural': 'Группы Дистрибьюторов',
                'db_table': 'distributor_group',
            },
        ),
        migrations.AddField(
            model_name='distributor',
            name='operation_type',
            field=models.CharField(choices=[('Domestic', 'Domestic'), ('Export', 'Export'), ('ПРОВЕРИТЬ', 'ПРОВЕРИТЬ')], default='ПРОВЕРИТЬ', max_length=50),
        ),
        migrations.AddField(
            model_name='distributor',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='metabase_wrapper.distributorgroup'),
        ),
    ]
