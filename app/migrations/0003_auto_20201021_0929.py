# Generated by Django 3.0.3 on 2020-10-21 01:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201021_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='user_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='camera',
            name='data',
            field=models.ImageField(blank=True, upload_to='image', verbose_name='当前数据'),
        ),
        migrations.AlterField(
            model_name='camera',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='camera',
            name='model_type',
            field=models.CharField(max_length=20, verbose_name='型号'),
        ),
        migrations.AlterField(
            model_name='camera',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 21, 9, 29, 25, 67042), verbose_name='运行时间'),
        ),
        migrations.AlterField(
            model_name='camera',
            name='state',
            field=models.BooleanField(blank=True, default=False, verbose_name='是否正常运行'),
        ),
        migrations.AlterField(
            model_name='fixlist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='fixlist',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 9, 29, 25, 71012), verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='humiditysensor',
            name='data',
            field=models.CharField(blank=True, max_length=20, verbose_name='当前数据'),
        ),
        migrations.AlterField(
            model_name='humiditysensor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='humiditysensor',
            name='model_type',
            field=models.CharField(max_length=20, verbose_name='型号'),
        ),
        migrations.AlterField(
            model_name='humiditysensor',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 21, 9, 29, 25, 67042), verbose_name='运行时间'),
        ),
        migrations.AlterField(
            model_name='humiditysensor',
            name='state',
            field=models.BooleanField(blank=True, default=False, verbose_name='是否正常运行'),
        ),
        migrations.AlterField(
            model_name='incubator',
            name='incubator_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='incubator',
            name='incubator_type',
            field=models.CharField(max_length=20, verbose_name='型号'),
        ),
        migrations.AlterField(
            model_name='incubator',
            name='state',
            field=models.BooleanField(default=True, verbose_name='是否正常运行'),
        ),
        migrations.AlterField(
            model_name='incubatorhistory',
            name='curTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 9, 29, 25, 71012), verbose_name='当前记录时间'),
        ),
        migrations.AlterField(
            model_name='incubatorhistory',
            name='humidity',
            field=models.CharField(blank=True, max_length=20, verbose_name='湿度'),
        ),
        migrations.AlterField(
            model_name='incubatorhistory',
            name='light',
            field=models.CharField(blank=True, max_length=20, verbose_name='光照强度'),
        ),
        migrations.AlterField(
            model_name='incubatorhistory',
            name='pressure',
            field=models.CharField(blank=True, max_length=20, verbose_name='压强'),
        ),
        migrations.AlterField(
            model_name='incubatorhistory',
            name='temperature',
            field=models.CharField(blank=True, max_length=20, verbose_name='温度'),
        ),
        migrations.AlterField(
            model_name='lightsensor',
            name='data',
            field=models.CharField(blank=True, max_length=20, verbose_name='当前数据'),
        ),
        migrations.AlterField(
            model_name='lightsensor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lightsensor',
            name='model_type',
            field=models.CharField(max_length=20, verbose_name='型号'),
        ),
        migrations.AlterField(
            model_name='lightsensor',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 21, 9, 29, 25, 62998), verbose_name='运行时间'),
        ),
        migrations.AlterField(
            model_name='lightsensor',
            name='state',
            field=models.BooleanField(blank=True, default=False, verbose_name='是否正常运行'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='mark',
            field=models.IntegerField(blank=True, verbose_name='评分'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(max_length=20, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='plant_type',
            field=models.CharField(max_length=20, verbose_name='种类'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='popularity',
            field=models.IntegerField(default=60, verbose_name='欢迎程度'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='state',
            field=models.CharField(blank=True, max_length=20, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='时长'),
        ),
        migrations.AlterField(
            model_name='pressuresensor',
            name='data',
            field=models.CharField(blank=True, max_length=20, verbose_name='当前数据'),
        ),
        migrations.AlterField(
            model_name='pressuresensor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pressuresensor',
            name='model_type',
            field=models.CharField(max_length=20, verbose_name='型号'),
        ),
        migrations.AlterField(
            model_name='pressuresensor',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 21, 9, 29, 25, 62998), verbose_name='运行时间'),
        ),
        migrations.AlterField(
            model_name='pressuresensor',
            name='state',
            field=models.BooleanField(blank=True, default=False, verbose_name='是否正常运行'),
        ),
        migrations.AlterField(
            model_name='temperaturesensor',
            name='data',
            field=models.CharField(blank=True, max_length=20, verbose_name='当前数据'),
        ),
        migrations.AlterField(
            model_name='temperaturesensor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='temperaturesensor',
            name='model_type',
            field=models.CharField(max_length=20, verbose_name='型号'),
        ),
        migrations.AlterField(
            model_name='temperaturesensor',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 21, 9, 29, 25, 67042), verbose_name='运行时间'),
        ),
        migrations.AlterField(
            model_name='temperaturesensor',
            name='state',
            field=models.BooleanField(blank=True, default=False, verbose_name='是否正常运行'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], db_column='userSex', default=0, max_length=20, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastLoginTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 9, 29, 25, 55016)),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 21, 9, 29, 25, 55016)),
        ),
        migrations.AlterModelTable(
            name='user',
            table='使用用户',
        ),
    ]
