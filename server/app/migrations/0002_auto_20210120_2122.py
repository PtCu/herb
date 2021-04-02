# Generated by Django 3.0.3 on 2021-01-20 21:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('user_name', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='姓名')),
                ('password', models.CharField(max_length=20)),
                ('img', models.ImageField(blank=True, upload_to='image')),
            ],
            options={
                'verbose_name': '管理员',
                'verbose_name_plural': '管理员',
                'db_table': 'Administrator',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity', models.CharField(default='', max_length=20, verbose_name='湿度')),
                ('temperature', models.CharField(default='', max_length=20, verbose_name='温度')),
                ('light', models.CharField(default='', max_length=20, verbose_name='光强')),
                ('pres', models.CharField(default='', max_length=20, verbose_name='压强')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('message', models.CharField(max_length=500, verbose_name='信息')),
                ('incubator_id', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '环境建议',
                'verbose_name_plural': '环境建议',
                'db_table': 'Advice',
                'ordering': ('time',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity', models.CharField(default='', max_length=20, verbose_name='湿度')),
                ('temperature', models.CharField(default='', max_length=20, verbose_name='温度')),
                ('light', models.CharField(default='', max_length=20, verbose_name='光强')),
                ('pres', models.CharField(default='', max_length=20, verbose_name='压强')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('incubator_id', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '控制信息',
                'verbose_name_plural': '控制信息',
                'db_table': 'Control',
                'ordering': ('time',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Incubator',
            fields=[
                ('incubator_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='培养箱ID')),
                ('incubator_type', models.CharField(max_length=20, verbose_name='型号')),
                ('state', models.BooleanField(default=True, verbose_name='是否正常运行')),
                ('key', models.CharField(default='111111', max_length=20, verbose_name='密钥')),
            ],
            options={
                'verbose_name': '培养箱',
                'verbose_name_plural': '培养箱',
                'db_table': 'Incubator',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(default='1', max_length=20, verbose_name='种类')),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('img', models.ImageField(blank=True, upload_to='image')),
                ('mark', models.IntegerField(blank=True, verbose_name='评分')),
                ('popularity', models.IntegerField(default=60, verbose_name='欢迎程度')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间')),
                ('state', models.CharField(blank=True, default='未知', max_length=20, verbose_name='状态')),
                ('isShow', models.IntegerField(default=False, verbose_name='是否允许发布')),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'verbose_name': '植物',
                'verbose_name_plural': '植物',
                'db_table': 'Plant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, unique=True, verbose_name='电话')),
                ('mail', models.CharField(max_length=20, verbose_name='邮箱')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('password', models.CharField(max_length=20)),
                ('img', models.ImageField(blank=True, upload_to='image')),
                ('gender', models.CharField(choices=[('男', '男'), ('女', '女')], db_column='userSex', default=0, max_length=20, verbose_name='性别')),
                ('lastLoginTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='上次登录时间')),
                ('signature', models.TextField(blank=True, null=True)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='注册时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'User',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='订单ID')),
                ('addr', models.CharField(default='未知', max_length=100, verbose_name='地址')),
                ('using', models.CharField(default='未知', max_length=1000, verbose_name='用途')),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='订单时间')),
                ('number', models.IntegerField(default=1, verbose_name='数量')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'db_table': 'UserOrder',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_type', models.CharField(max_length=20, verbose_name='传感器类型')),
                ('sensor_name', models.CharField(max_length=20, verbose_name='传感器名称')),
                ('sensor_state', models.BooleanField(default=True, verbose_name='传感器状态')),
                ('delivery_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='出厂时间')),
                ('service_life', models.IntegerField(default=24, verbose_name='使用寿命')),
                ('sensor_value', models.CharField(default='0', max_length=20, verbose_name='传感器数值')),
                ('incubator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'verbose_name': '传感器',
                'verbose_name_plural': '传感器',
                'db_table': 'Sensor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlantDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=20, verbose_name='植物名')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('effect', models.CharField(max_length=100, verbose_name='功效')),
                ('place', models.CharField(max_length=100, verbose_name='产地')),
                ('shape', models.CharField(max_length=1000, verbose_name='植物形态')),
                ('taboo', models.CharField(max_length=100, verbose_name='使用禁忌')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Plant')),
            ],
            options={
                'verbose_name': '植物详情',
                'verbose_name_plural': '植物详情',
                'db_table': 'PlantDetail',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='IncubatorHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='当前记录时间')),
                ('light', models.CharField(blank=True, max_length=20, verbose_name='光照强度')),
                ('pressure', models.CharField(blank=True, max_length=20, verbose_name='压强')),
                ('humidity', models.CharField(blank=True, max_length=20, verbose_name='湿度')),
                ('temperature', models.CharField(blank=True, max_length=20, verbose_name='温度')),
                ('plant', models.CharField(default='人参', max_length=20, verbose_name='植物')),
                ('image', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='图片')),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'verbose_name': '历史记录',
                'verbose_name_plural': '历史记录',
                'db_table': 'IncubatorHistory',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='incubator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.CreateModel(
            name='FixList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='订单号')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('state', models.BooleanField(default=False, verbose_name='维修状态')),
                ('address', models.CharField(default='ttt', max_length=100, verbose_name='地址')),
                ('describe', models.CharField(default='uuu', max_length=200, verbose_name='故障描述')),
                ('phone', models.CharField(default='10086', max_length=20, verbose_name='联系电话')),
                ('incubator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'verbose_name': '维修订单',
                'verbose_name_plural': '维修订单',
                'db_table': 'FixList',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(max_length=20, verbose_name='设备型号')),
                ('device_name', models.CharField(max_length=20, verbose_name='设备名')),
                ('device_state', models.BooleanField(default=True, verbose_name='设备状态')),
                ('delivery_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='出厂日期')),
                ('service_life', models.IntegerField(default=24, verbose_name='使用寿命')),
                ('incubator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'verbose_name': '外部设备',
                'verbose_name_plural': '外部设备',
                'db_table': 'Device',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('model_type', models.CharField(max_length=20, verbose_name='型号')),
                ('state', models.BooleanField(blank=True, default=False, verbose_name='是否正常运行')),
                ('start_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='运行时间')),
                ('data', models.ImageField(blank=True, upload_to='image', verbose_name='当前数据')),
                ('incubator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Incubator')),
            ],
            options={
                'verbose_name': '照相机',
                'verbose_name_plural': '照相机',
                'db_table': 'Camera',
                'managed': True,
            },
        ),
    ]
