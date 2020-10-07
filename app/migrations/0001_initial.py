# Generated by Django 3.0.3 on 2020-10-07 13:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incubator',
            fields=[
                ('incubator_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('state', models.BooleanField()),
            ],
            options={
                'db_table': 'Incubator',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=15)),
                ('mail', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='image')),
                ('gender', models.NullBooleanField()),
                ('lastLoginTime', models.DateTimeField()),
                ('signature', models.TextField(blank=True, null=True)),
                ('registration_date', models.DateTimeField(default=datetime.datetime(2020, 10, 7, 21, 31, 11, 322176))),
            ],
            options={
                'db_table': 'User',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TemperatureSensor',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('model_type', models.CharField(max_length=20)),
                ('state', models.BooleanField()),
                ('start_time', models.DateTimeField()),
                ('data', models.CharField(max_length=20)),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'db_table': 'TemperatureSensor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PressureSensor',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('model_type', models.CharField(max_length=20)),
                ('state', models.BooleanField()),
                ('start_time', models.DateTimeField()),
                ('data', models.CharField(max_length=20)),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'db_table': 'PressureSensor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('plant_type', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='image')),
                ('mark', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'db_table': 'Plant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LightSensor',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('model_type', models.CharField(max_length=20)),
                ('state', models.BooleanField()),
                ('start_time', models.DateTimeField()),
                ('data', models.CharField(max_length=20)),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'db_table': 'LightSensor',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='incubator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.CreateModel(
            name='HumiditySensor',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('model_type', models.CharField(max_length=20)),
                ('state', models.BooleanField()),
                ('start_time', models.DateTimeField()),
                ('data', models.CharField(max_length=20)),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'db_table': 'HumiditySensor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FixList',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'db_table': 'FixList',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('model_type', models.CharField(max_length=20)),
                ('state', models.BooleanField()),
                ('start_time', models.DateTimeField()),
                ('data', models.CharField(max_length=20)),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'db_table': 'Camera',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='IncubatorHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curTime', models.DateTimeField()),
                ('light', models.CharField(max_length=20)),
                ('pressure', models.CharField(max_length=20)),
                ('humidity', models.CharField(max_length=20)),
                ('temperature', models.CharField(max_length=20)),
                ('plant', models.CharField(max_length=20)),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'db_table': 'IncubatorHistory',
                'managed': True,
                'unique_together': {('curTime', 'incubator')},
            },
        ),
    ]
