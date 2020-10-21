from datetime import datetime
from django.db import models


class User(models.Model):
    user_id = models.AutoField("ID",primary_key=True)
    phone = models.CharField("电话",max_length=15,unique=True)
    mail = models.CharField("邮箱",max_length=20)
    name = models.CharField("姓名",max_length=10)
    password = models.CharField(max_length=20)
    img = models.ImageField(upload_to='image', blank=True)  # 图像
    gender = models.CharField("性别",db_column='userSex', choices=(('男', '男'), ('女', '女')), default=0, max_length=20)
    lastLoginTime = models.DateTimeField(default=datetime.now())
    signature = models.TextField(null=True, blank=True) #个性签名
    registration_date = models.DateTimeField(default=datetime.now()) #创建时间

    def __str__(self):
            return '使用用户'+self.name+str(self.user_id)

    class Meta:
        managed = True
        db_table = 'User'
        verbose_name = '使用用户'
        verbose_name_plural = '使用用户'

class Administrator(models.Model):
    user_name = models.CharField("姓名",primary_key=True,max_length=20)
    password = models.CharField(max_length=20)
    img = models.ImageField(upload_to='image', blank=True)  # 图像

    class Meta:
        managed = True
        db_table = 'Administrator'



class Incubator(models.Model):

    incubator_id = models.AutoField("ID",primary_key=True)
    incubator_type = models.CharField("型号",max_length=20) #型号
    state = models.BooleanField("是否正常运行",default=True)  # 是否正常运行
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)  # 培养箱的用户（一个用户可以多个培养箱）

    class Meta:
        managed = True
        db_table = 'Incubator'
        verbose_name = '培养箱'
        verbose_name_plural = '培养箱'

    def __str__(self):
                return '培养箱'+str(self.incubator_id)

class LightSensor(models.Model):
    id = models.AutoField("ID",primary_key=True)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField("型号",max_length=20)  # 型号
    state = models.BooleanField("是否正常运行",default=False, blank=True)  # 是否坏了
    start_time = models.DateTimeField("运行时间",
        default=datetime.now(), blank=True)  # 开始运行时间
    data = models.CharField("当前数据",max_length=20, blank=True)  # 当前数据

    class Meta:
        managed = True
        db_table = 'LightSensor'
        verbose_name = '光照传感器'
        verbose_name_plural = '光照传感器'


    def __str__(self):
                return '光照传感器' + str(self.id)
                
class PressureSensor(models.Model):
    id = models.AutoField("ID",primary_key=True)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField("型号",max_length=20)  # 型号
    state = models.BooleanField("是否正常运行",default=False, blank=True)  # 是否坏了
    start_time = models.DateTimeField("运行时间",
        default=datetime.now(), blank=True)  # 开始运行时间
    data = models.CharField("当前数据",max_length=20, blank=True)  # 当前数据

    class Meta:
        managed = True
        db_table = 'PressureSensor'
        verbose_name = '压强传感器'
        verbose_name_plural = '压强传感器'

    def __str__(self):
                return '压强传感器' + str(self.id)

class TemperatureSensor(models.Model):
    id = models.AutoField("ID",primary_key=True)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField("型号",max_length=20)  # 型号
    state = models.BooleanField("是否正常运行",default=False, blank=True)  # 是否坏了
    start_time = models.DateTimeField("运行时间",
        default=datetime.now(), blank=True)  # 开始运行时间
    data = models.CharField("当前数据",max_length=20, blank=True)  # 当前数据

    class Meta:
        managed = True
        db_table = 'TemperatureSensor'
        verbose_name = '温度传感器'
        verbose_name_plural = '温度传感器'

    def __str__(self):
                return '温度传感器' + str(self.id)

class HumiditySensor(models.Model):
    id = models.AutoField("ID",primary_key=True)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField("型号",max_length=20)  # 型号
    state = models.BooleanField("是否正常运行",default=False, blank=True)  # 是否坏了
    start_time = models.DateTimeField("运行时间",
        default=datetime.now(), blank=True)  # 开始运行时间
    data = models.CharField("当前数据",max_length=20, blank=True)  # 当前数据

    class Meta:
        managed = True
        db_table = 'HumiditySensor'
        verbose_name = '湿度传感器'
        verbose_name_plural = '湿度传感器'

    def __str__(self):
                return '湿度传感器' + str(self.id)

class Camera(models.Model):
    id = models.AutoField("ID",primary_key=True)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField("型号",max_length=20)  # 型号
    state = models.BooleanField("是否正常运行",default=False, blank=True)  # 是否坏了
    start_time = models.DateTimeField("运行时间",
        default=datetime.now(), blank=True)  # 开始运行时间
    data = models.ImageField("当前数据",upload_to='image', blank=True)  # 当前数据

    class Meta:
        managed = True
        db_table = 'Camera'
        verbose_name = '照相机'
        verbose_name_plural = '照相机'

    def __str__(self):
                return '照相机' + str(self.id)

class Plant(models.Model):
    id = models.AutoField("ID",primary_key=True)
    plant_type = models.CharField("种类",max_length=20)  # 植物的种类
    name = models.CharField("名字",max_length=20)  # 名字
    img = models.ImageField(upload_to='image',blank=True)  # 图像
    mark = models.IntegerField("评分",blank=True)  # 评分
    popularity = models.IntegerField("欢迎程度",default=60)
    time = models.DateTimeField("时长",auto_now=True)
    state = models.CharField("状态",max_length=20,blank=True)  # 开花结果
    # 培养箱 (一个培养箱可以多个植物，但需要保证为一种)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'Plant'
        verbose_name = '植物'
        verbose_name_plural = '植物'

    def __str__(self):
                return '植株' + self.plant_name+'-'+str(self.id)
# 真正用来存储传感器数据的表
# 查找植物历史状态时，先查培养箱表，再获取当前植物以获取植物名称


class IncubatorHistory(models.Model):
    curTime = models.DateTimeField("当前记录时间",default=datetime.now())  # 定时存入数据库的时间
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 对应的培养箱
    light = models.CharField("光照强度",max_length=20, blank=True)  # 光强
    pressure = models.CharField("压强",max_length=20, blank=True)  # 压强
    humidity = models.CharField("湿度",max_length=20, blank=True)
    temperature = models.CharField("温度",max_length=20, blank=True)
    plant = models.CharField(max_length=20, blank=True)  # 植物

    class Meta:
        unique_together = ("curTime", "incubator")
        managed = True
        db_table = 'IncubatorHistory'
        verbose_name = '历史记录'
        verbose_name_plural = '历史记录'

    def __str__(self):
                return '历史记录' + self.curTime+'-'+self.incubator

# 用户维修设备逻辑：用户查看自己的sensor state，如果坏了就点击提交
# 提交受理后生成维修订单。维修订单信息包括id和时间，以及培养箱编号


class FixList(models.Model):
    id = models.AutoField("订单号",primary_key=True)  # 订单编号
    time = models.DateTimeField("时间",default=datetime.now())  # 订单生成时间
    # 培养箱 #django 1对多时，foreigneKey在多的一方
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'FixList'
        verbose_name = '维修订单'
        verbose_name_plural = '维修订单'

    def __str__(self):
            return '维修信息' + str(self.id)+'-'+self.time