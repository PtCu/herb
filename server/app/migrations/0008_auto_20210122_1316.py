# Generated by Django 3.0.3 on 2021-01-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210121_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensor_type',
            field=models.CharField(default='s1', max_length=20, verbose_name='传感器类型'),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='schedule',
            field=models.CharField(choices=[('申请中，待通过', '申请中，待通过'), ('配送中', '配送中'), ('正在使用', '正在使用'), ('信息不全，拒绝通过', '信息不全，拒绝通过')], default='申请中，待通过', max_length=20, verbose_name='订单状态'),
        ),
    ]
