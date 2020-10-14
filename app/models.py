from datetime import datetime
from django.db import models


class User(models.Model):
    user_id = models.CharField(primary_key=True,max_length=20)
    phone = models.CharField(max_length=15)
    mail = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    img = models.ImageField(upload_to='image')  # 图像
    gender = models.CharField(db_column='userSex', choices=(('男', '男'), ('女', '女')), default=0, max_length=20)
    lastLoginTime = models.DateTimeField()
    signature = models.TextField(null=True, blank=True) #个性签名
    registration_date = models.DateTimeField(default=datetime.now()) #创建时间

    class Meta:
        managed = True
        db_table = 'User'


class Incubator(models.Model):
    incubator_id = models.CharField(primary_key=True, max_length=20)
    incubator_type = models.CharField(max_length=20) #型号
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
    img = models.ImageField(upload_to='image')  # 图像
    mark = models.IntegerField()  # 评分
    state = models.CharField(max_length=20)  # 开花结果
    # 培养箱 (一个培养箱可以多个植物，但需要保证为一种)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'Plant'

# 真正用来存储传感器数据的表
# 查找植物历史状态时，先查培养箱表，再获取当前植物以获取植物名称


class IncubatorHistory(models.Model):
    curTime = models.DateTimeField()  # 定时存入数据库的时间
    incubator = models.ForeignKey(
        Incubator, on_delete=models.CASCADE)  # 对应的培养箱
    light = models.CharField(max_length=20)  # 光强
    pressure = models.CharField(max_length=20)  # 压强
    humidity = models.CharField(max_length=20)
    temperature = models.CharField(max_length=20)
    plant = models.CharField(max_length=20)  # 植物

    class Meta:
        unique_together = ("curTime", "incubator")
        managed = True
        db_table = 'IncubatorHistory'

# 用户维修设备逻辑：用户查看自己的sensor state，如果坏了就点击提交
# 提交受理后生成维修订单。维修订单信息包括id和时间，以及培养箱编号


class FixList(models.Model):
    id = models.CharField(primary_key=True, max_length=20)  # 订单编号
    time = models.DateTimeField(default=datetime.now())  # 订单生成时间
    # 培养箱 #django 1对多时，foreigneKey在多的一方
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'FixList'
