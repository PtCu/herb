from datetime import datetime
from django.db import models


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    phone = models.CharField(max_length=15)
    mail = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    img = models.ImageField(upload_to='image')  # 图像
    gender = models.CharField(db_column='userSex', choices=(('男', '男'), ('女', '女')), default=0, max_length=20)
    lastLoginTime = models.DateTimeField()
    signature = models.TextField(null=True, blank=True)  # 个性签名
    registration_date = models.DateTimeField(default=datetime.now())  # 创建时间

    class Meta:
        managed = True
        db_table = 'User'


class Incubator(models.Model):
    incubator_id = models.CharField(primary_key=True, max_length=20)
    incubator_type = models.CharField(max_length=20)  # 型号
    state = models.BooleanField()  # 是否正常运行
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)  # 培养箱的用户（一个用户可以多个培养箱）

    class Meta:
        managed = True
        db_table = 'Incubator'


class LightSensor(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField(max_length=20)  # 型号
    state = models.BooleanField()  # 是否坏了
    start_time = models.DateTimeField()  # 开始运行时间
    data = models.CharField(max_length=20)  # 当前数据

    class Meta:
        managed = True
        db_table = 'LightSensor'


class PressureSensor(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField(max_length=20)  # 型号
    state = models.BooleanField()  # 是否坏了
    start_time = models.DateTimeField()  # 开始运行时间
    data = models.CharField(max_length=20)  # 当前数据

    class Meta:
        managed = True
        db_table = 'PressureSensor'


class TemperatureSensor(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField(max_length=20)  # 型号
    state = models.BooleanField()  # 是否坏了
    start_time = models.DateTimeField()  # 开始运行时间
    data = models.CharField(max_length=20)  # 当前数据

    class Meta:
        managed = True
        db_table = 'TemperatureSensor'


class HumiditySensor(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField(max_length=20)  # 型号
    state = models.BooleanField()  # 是否坏了
    start_time = models.DateTimeField()  # 开始运行时间
    data = models.CharField(max_length=20)  # 当前数据

    class Meta:
        managed = True
        db_table = 'HumiditySensor'


class Camera(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField(max_length=20)  # 型号
    state = models.BooleanField()  # 是否坏了
    start_time = models.DateTimeField()  # 开始运行时间
    data = models.CharField(max_length=20)  # 当前数据

    class Meta:
        managed = True
        db_table = 'Camera'


class Plant(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    plant_type = models.CharField(max_length=20)  # 植物的种类
    name = models.CharField(max_length=20)  # 名字
    img = models.ImageField(upload_to=None, default='avator.jpg')  # 图像
    mark = models.IntegerField()  # 评分
    popularity = models.IntegerField(default=60)
    time = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=20)  # 开花结果
    # 培养箱 (一个培养箱可以多个植物，但需要保证为一种)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'Plant'


# 真正用来存储传感器数据的表
# 查找植物历史状态时，先查培养箱表，再获取当前植物以获取植物名称


class IncubatorHistory(models.Model):
    curTime = models.DateTimeField(default=datetime.now)  # 定时存入数据库的时间
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 对应的培养箱
    light = models.CharField(max_length=20)  # 光强
    pressure = models.CharField(max_length=20)  # 压强
    humidity = models.CharField(max_length=20)
    temperature = models.CharField(max_length=20)
    plant = models.CharField(max_length=20)  # 植物
    image = models.ImageField(upload_to=None, blank=True, null=True)

    class Meta:
        unique_together = ("curTime", "incubator")
        managed = True
        db_table = 'IncubatorHistory'


# 用户维修设备逻辑：用户查看自己的sensor state，如果坏了就点击提交
# 提交受理后生成维修订单。维修订单信息包括id和时间，以及培养箱编号


class FixList(models.Model):
    time = models.DateTimeField(default=datetime.now())  # 订单生成时间
    state = models.BooleanField(default=False)
    # 培养箱 #django 1对多时，foreigneKey在多的一方
    incubator_id = models.ForeignKey(Incubator, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'FixList'


class Control(models.Model):
    # 用于存放用户控制培养箱的信息
    humidity = models.CharField(max_length=20, default="")
    temperature = models.CharField(max_length=20, default="")
    light = models.CharField(max_length=20, default="")
    pres = models.CharField(max_length=20, default='')

    time = models.DateTimeField(default=datetime.now)
    incubator_id = models.CharField(max_length=20)

    class Meta:
        ordering = ("time",)
        managed = True
        db_table = 'Control'


class Advice(models.Model):
    # 用于存放建议信息
    humidity = models.CharField(max_length=20, default="")
    temperature = models.CharField(max_length=20, default="")
    light = models.CharField(max_length=20, default="")
    pres = models.CharField(max_length=20, default='')
    time = models.DateTimeField(default=datetime.now)
    message = models.CharField(max_length=500)
    incubator_id = models.CharField(max_length=20)

    class Meta:
        ordering = ("time",)
        managed = True
        db_table = 'Advice'


class Sensor(models.Model):
    # 传感器列表
    incubator_id = models.ForeignKey(Incubator, on_delete=models.CASCADE)
    sensor_type = models.CharField(max_length=20)  # 传感器型号
    sensor_name = models.CharField(max_length=20)  # 传感器名称
    sensor_state = models.BooleanField(default=True)  # 传感器开关 默认为开
    delivery_time = models.DateTimeField(default="2020-01-01 00:00:00")  # 出厂时间
    service_life = models.IntegerField(default=24)  # 使用寿命 默认两年
    sensor_value = models.CharField(max_length=20,default='0')  # 传感器当前值

    class Meta:
        managed = True
        db_table = 'Sensor'


class Device(models.Model):
    # 设备列表（目前暂时用于存储像CPU,显示屏等与改变环境无关的设备）
    incubator_id = models.ForeignKey(Incubator, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=20)  # 设备型号
    device_name = models.CharField(max_length=20)  # 设备名称
    # 设备开关暂时去除，考虑到后续调节温湿度
    device_state = models.BooleanField(default=True)  # 开关 默认为开
    delivery_time = models.DateTimeField(default="2020-01-01 00:00:00")  # 出厂时间
    service_life = models.IntegerField(default=24)  # 使用寿命 默认两年

    class Meta:
        managed = True
        db_table = 'Device'


