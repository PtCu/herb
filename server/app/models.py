from datetime import datetime

import django
from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.CharField("ID", primary_key=True, max_length=20)
    phone = models.CharField("电话", max_length=15, unique=True)
    mail = models.CharField("邮箱", max_length=20)
    name = models.CharField("姓名", max_length=10)
    password = models.CharField(max_length=20)
    img = models.ImageField(upload_to='static/img/personInfo', blank=True, default="avator.jpg")  # 图像
    gender = models.CharField("性别", db_column='userSex', choices=(('男', '男'), ('女', '女')), default=0, max_length=20)
    lastLoginTime = models.DateTimeField("上次登录时间", default=django.utils.timezone.now)
    signature = models.TextField(null=True, blank=True)  # 个性签名
    registration_date = models.DateTimeField("注册时间", default=django.utils.timezone.now)  # 创建时间

    def __str__(self):
        return '用户' + str(self.user_id)

    class Meta:
        managed = True
        db_table = 'User'
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Administrator(models.Model):
    user_name = models.CharField("姓名", primary_key=True, max_length=20)
    password = models.CharField(max_length=20)
    img = models.ImageField(upload_to='image', blank=True)  # 图像

    class Meta:
        managed = True
        db_table = 'Administrator'
        verbose_name = '管理员'
        verbose_name_plural = '管理员'


class Incubator(models.Model):
    incubator_id = models.CharField("培养箱ID", primary_key=True, max_length=20)
    incubator_type = models.CharField("型号", max_length=20, default='ZY-001')  # 型号
    state = models.BooleanField("是否正常运行", default=False)  # 是否正常运行
    schedule = models.CharField("培养箱情况", choices=(('用户申请中，待通过', '用户申请中，待通过'),
                                                  ('配送中', '配送中'),
                                                  ('正在使用', '正在使用')), default='正在使用', max_length=20)
    key = models.CharField("密钥", max_length=20, default='111111')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 培养箱的用户（一个用户可以多个培养箱）
    ip_address = models.GenericIPAddressField(default='127.0.0.1')

    class Meta:
        managed = True
        db_table = 'Incubator'
        verbose_name = '培养箱'
        verbose_name_plural = '培养箱'

    def __str__(self):
        return '培养箱' + str(self.incubator_id)


'''
class LightSensor(models.Model):
    id = models.AutoField("ID", primary_key=True)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField("型号", max_length=20)  # 型号
    state = models.BooleanField("是否正常运行", default=False, blank=True)  # 是否坏了
    start_time = models.DateTimeField("运行时间",
                                      default=django.utils.timezone.now, blank=True)  # 开始运行时间
    data = models.CharField("当前数据", max_length=20, blank=True)  # 当前数据

    class Meta:
        managed = True
        db_table = 'LightSensor'
        verbose_name = '光照传感器'
        verbose_name_plural = '光照传感器'

    def __str__(self):
        return '光照传感器' + str(self.id)


class PressureSensor(models.Model):
    id = models.AutoField("ID", primary_key=True)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField("型号", max_length=20)  # 型号
    state = models.BooleanField("是否正常运行", default=False, blank=True)  # 是否坏了
    start_time = models.DateTimeField("运行时间",
                                      default=django.utils.timezone.now, blank=True)  # 开始运行时间
    data = models.CharField("当前数据", max_length=20, blank=True)  # 当前数据

    class Meta:
        managed = True
        db_table = 'PressureSensor'
        verbose_name = '压强传感器'
        verbose_name_plural = '压强传感器'

    def __str__(self):
        return '压强传感器' + str(self.id)


class TemperatureSensor(models.Model):
    id = models.AutoField("ID", primary_key=True)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField("型号", max_length=20)  # 型号
    state = models.BooleanField("是否正常运行", default=False, blank=True)  # 是否坏了
    start_time = models.DateTimeField("运行时间",
                                      default=django.utils.timezone.now, blank=True)  # 开始运行时间
    data = models.CharField("当前数据", max_length=20, blank=True)  # 当前数据

    class Meta:
        managed = True
        db_table = 'TemperatureSensor'
        verbose_name = '温度传感器'
        verbose_name_plural = '温度传感器'

    def __str__(self):
        return '温度传感器' + str(self.id)


class HumiditySensor(models.Model):
    id = models.AutoField("ID", primary_key=True)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField("型号", max_length=20)  # 型号
    state = models.BooleanField("是否正常运行", default=False, blank=True)  # 是否坏了
    start_time = models.DateTimeField("运行时间",
                                      default=django.utils.timezone.now, blank=True)  # 开始运行时间
    data = models.CharField("当前数据", max_length=20, blank=True)  # 当前数据

    class Meta:
        managed = True
        db_table = 'HumiditySensor'
        verbose_name = '湿度传感器'
        verbose_name_plural = '湿度传感器'

    def __str__(self):
        return '湿度传感器' + str(self.id)
'''


class Camera(models.Model):
    id = models.AutoField("ID", primary_key=True)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 箱子
    model_type = models.CharField("型号", max_length=20)  # 型号
    state = models.BooleanField("是否正常运行", default=False, blank=True)  # 是否坏了
    start_time = models.DateTimeField("运行时间", default=django.utils.timezone.now, blank=True)  # 开始运行时间
    data = models.ImageField("当前数据", upload_to='image', blank=True)  # 当前数据

    class Meta:
        managed = True
        db_table = 'Camera'
        verbose_name = '照相机'
        verbose_name_plural = '照相机'

    def __str__(self):
        return '照相机' + str(self.id)


class Plant(models.Model):
    id = models.AutoField("ID", primary_key=True)
    plant_type = models.CharField("种类", max_length=20, default='1')  # 植物的种类
    name = models.CharField("名字", max_length=20)  # 名字
    img = models.ImageField(upload_to='image', blank=True)  # 图像
    mark = models.IntegerField("评分", blank=True)  # 评分
    popularity = models.IntegerField("欢迎程度", default=60)
    time = models.DateTimeField("提交时间", default=django.utils.timezone.now)
    state = models.CharField("状态", max_length=20, blank=True, default="未知")  # 开花结果
    # isShow = models.IntegerField("是否允许发布", default=False)
    isShow = models.CharField("是否允许发布", choices=(('是', '是'), ('否', '否')), default='否', max_length=20)
    # 培养箱 (一个培养箱可以多个植物，但需要保证为一种)
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'Plant'
        verbose_name = '植物'
        verbose_name_plural = '植物'

    def __str__(self):
        return '植株'


# 真正用来存储传感器数据的表
# 查找植物历史状态时，先查培养箱表，再获取当前植物以获取植物名称


class IncubatorHistory(models.Model):
    curTime = models.DateTimeField("当前记录时间", default=django.utils.timezone.now)  # 定时存入数据库的时间
    incubator = models.ForeignKey(Incubator, on_delete=models.CASCADE)  # 对应的培养箱
    light = models.CharField("光照强度", max_length=20, blank=True)  # 光强
    pressure = models.CharField("压强", max_length=20, blank=True)  # 压强
    humidity = models.CharField("湿度", max_length=20, blank=True)
    temperature = models.CharField("温度", max_length=20, blank=True)
    plant = models.CharField("植物", max_length=20, default='人参')  # 植物
    image = models.ImageField("图片", upload_to=None, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'IncubatorHistory'
        verbose_name = '历史记录'
        verbose_name_plural = '历史记录'

    def __str__(self):
        return '历史记录'


# 用户维修设备逻辑：用户查看自己的sensor state，如果坏了就点击提交
# 提交受理后生成维修订单。维修订单信息包括id和时间，以及培养箱编号


class FixList(models.Model):
    id = models.AutoField("订单号", primary_key=True)  # 订单编号
    time = models.DateTimeField("时间", default=django.utils.timezone.now)  # 订单生成时间
    # 培养箱 #django 1对多时，foreigneKey在多的一方
    state = models.BooleanField("维修状态", default=False)
    address = models.CharField("地址", max_length=100, default="ttt")
    describe = models.CharField("故障描述", max_length=200, default='uuu')
    phone = models.CharField("联系电话", max_length=20, default='10086')
    incubator_id = models.ForeignKey(Incubator, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'FixList'
        verbose_name = '维修订单'
        verbose_name_plural = '维修订单'

    def __str__(self):
        return '维修信息' + str(self.id) + '-' + str(self.time)


class Control(models.Model):
    # 用于存放用户控制培养箱的信息
    humidity = models.CharField("湿度", max_length=20, default="")
    temperature = models.CharField("温度", max_length=20, default="")
    light = models.CharField("光强", max_length=20, default="")
    pres = models.CharField("压强", max_length=20, default='')
    time = models.DateTimeField("时间", default=django.utils.timezone.now)
    incubator_id = models.CharField(max_length=20)

    class Meta:
        ordering = ("time",)
        managed = True
        db_table = 'Control'
        verbose_name = '控制信息'
        verbose_name_plural = '控制信息'

    def __str__(self):
        return '历史记录' + str(self.incubator_id)


class Advice(models.Model):
    # 用于存放建议信息
    humidity = models.CharField("湿度", max_length=20, default="")
    temperature = models.CharField("温度", max_length=20, default="")
    light = models.CharField("光强", max_length=20, default="")
    pres = models.CharField("压强", max_length=20, default='')
    time = models.DateTimeField("时间", default=django.utils.timezone.now)
    message = models.CharField("信息", max_length=500)
    incubator_id = models.CharField(max_length=20)

    class Meta:
        ordering = ("time",)
        managed = True
        db_table = 'Advice'
        verbose_name = '环境建议'
        verbose_name_plural = '环境建议'

    def __str__(self):
        return '环境建议' + str(self.incubator_id)


class Sensor(models.Model):
    # 传感器列表
    incubator_id = models.ForeignKey(Incubator, on_delete=models.CASCADE)
    sensor_type = models.CharField("传感器类型", max_length=20, default='s1')  # 传感器型号
    sensor_name = models.CharField("传感器名称", max_length=20)  # 传感器名称
    sensor_state = models.BooleanField("传感器状态", default=True)  # 传感器开关 默认为开
    delivery_time = models.DateTimeField("出厂时间", default=django.utils.timezone.now)  # 出厂时间
    service_life = models.IntegerField("使用寿命", default=24)  # 使用寿命 默认两年
    sensor_value = models.CharField("传感器数值", max_length=20, default='0')  # 传感器当前值

    class Meta:
        managed = True
        db_table = 'Sensor'
        verbose_name = '传感器'
        verbose_name_plural = '传感器'

    def __str__(self):
        return '传感器' + str(self.incubator_id)


class Device(models.Model):
    # 设备列表（目前暂时用于存储像CPU,显示屏等与改变环境无关的设备）
    incubator_id = models.ForeignKey(Incubator, on_delete=models.CASCADE)
    device_type = models.CharField("设备型号", max_length=20)  # 设备型号
    device_name = models.CharField("设备名", max_length=20)  # 设备名称
    # 设备开关暂时去除，考虑到后续调节温湿度
    device_state = models.BooleanField("设备状态", default=True)  # 开关 默认为开
    delivery_time = models.DateTimeField("出厂日期", default=django.utils.timezone.now)  # 出厂时间
    service_life = models.IntegerField("使用寿命", default=24)  # 使用寿命 默认两年

    class Meta:
        managed = True
        db_table = 'Device'
        verbose_name = '外部设备'
        verbose_name_plural = '外部设备'

    def __str__(self):
        return '外部设备' + str(self.incubator_id)


class UserOrder(models.Model):
    id = models.AutoField("订单ID", primary_key=True)
    addr = models.CharField('地址', max_length=100, default='未知')
    using = models.CharField('用途', max_length=1000, default='未知')
    order_time = models.DateTimeField("订单时间", default=django.utils.timezone.now)
    number = models.IntegerField("数量", default=1)
    phone = models.CharField('电话号码', default='未知', max_length=20)
    career = models.CharField("职业", choices=(('药农', '药农'),
                                             ('教师', '教师'),
                                             ('技术人员', '技术人员'),
                                             ('学生', '学生'),
                                             ('游客', '游客'),
                                             ('其他', '其他')), default='其他', max_length=20)
    schedule = models.CharField("订单状态", choices=(('申请中，待通过', '申请中，待通过'),
                                                 ('配送中', '配送中'),
                                                 ('正在使用', '正在使用'),
                                                 ('信息不全，拒绝通过', '信息不全，拒绝通过')), default='申请中，待通过', max_length=20)
    company_or_school = models.CharField('公司或学校', max_length=100, default='未知')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'UserOrder'
        verbose_name = '订单'
        verbose_name_plural = '订单'

    def __str__(self):
        return '订单' + str(self.id)


class PlantDetail(models.Model):
    id = models.AutoField("ID", primary_key=True)
    plant_name = models.CharField("植物名", max_length=20)
    create_time = models.DateTimeField("创建时间", default=django.utils.timezone.now)
    effect = models.CharField("功效", max_length=100)
    place = models.CharField("产地", max_length=100)
    shape = models.CharField("植物形态", max_length=1000)
    taboo = models.CharField('使用禁忌', max_length=100)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'PlantDetail'
        verbose_name = '植物详情'
        verbose_name_plural = '植物详情'

    def __str__(self):
        return '植物详情' + str(self.id)


class OrderIssue(models.Model):
    id = models.AutoField("ID", primary_key=True)
    name = models.CharField("姓名", default='未知', max_length=20)
    create_time = models.DateTimeField("创建时间", default=django.utils.timezone.now)
    email = models.CharField("邮箱", default='未知', max_length=50)
    phone = models.CharField('电话', default='未知', max_length=20)
    describe = models.CharField("反馈描述", default='未知', max_length=1000)
    issue_state = models.CharField("状态", choices=(('未处理', '未处理'), ('已处理', '已处理')), default='未处理', max_length=20)
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'OrderIssue'
        verbose_name = '申请反馈'
        verbose_name_plural = '申请反馈'

    def __str__(self):
        return '申请反馈' + str(self.id)
