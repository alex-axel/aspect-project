# Generated by Django 4.1.3 on 2022-11-06 19:34

from django.db import migrations, models
import django.db.models.deletion
import metabase_wrapper.models


class Migration(migrations.Migration):

    dependencies = [
        ('metabase_wrapper', '0008_rename_distriutor_sofile_distributor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Канал 1',
                'verbose_name_plural': 'Канал 1',
                'db_table': 'channel_1',
            },
        ),
        migrations.CreateModel(
            name='Channel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Канал 2',
                'verbose_name_plural': 'Канал 2',
                'db_table': 'channel_2',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Format1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Формат 1',
                'verbose_name_plural': 'Формат 1',
                'db_table': 'format_1',
            },
        ),
        migrations.CreateModel(
            name='Format2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Формат 2',
                'verbose_name_plural': 'Формат 2',
                'db_table': 'format_2',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('department', models.ForeignKey(default=metabase_wrapper.models.get_default_department, on_delete=models.SET(metabase_wrapper.models.get_default_department), to='metabase_wrapper.department')),
                ('head', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='metabase_wrapper.manager')),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
                'db_table': 'manager',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_code', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('channel_1', models.ForeignKey(default=metabase_wrapper.models.get_default_channel1, on_delete=models.SET(metabase_wrapper.models.get_default_channel1), to='metabase_wrapper.channel1')),
                ('channel_2', models.ForeignKey(default=metabase_wrapper.models.get_default_channel2, on_delete=models.SET(metabase_wrapper.models.get_default_channel2), to='metabase_wrapper.channel2')),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metabase_wrapper.distributor')),
                ('format_1', models.ForeignKey(default=metabase_wrapper.models.get_default_format1, on_delete=models.SET(metabase_wrapper.models.get_default_format1), to='metabase_wrapper.format1')),
                ('format_2', models.ForeignKey(default=metabase_wrapper.models.get_default_format2, on_delete=models.SET(metabase_wrapper.models.get_default_format2), to='metabase_wrapper.format2')),
                ('manager', models.ForeignKey(default=metabase_wrapper.models.get_default_manger, on_delete=models.SET(metabase_wrapper.models.get_default_manger), to='metabase_wrapper.manager')),
            ],
            options={
                'verbose_name': 'Торговая точка',
                'verbose_name_plural': 'Торговые точки',
                'db_table': 'shop',
                'unique_together': {('name', 'address')},
            },
        ),
    ]
