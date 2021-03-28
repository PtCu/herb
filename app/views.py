import base64
import os
import random
from datetime import datetime
from typing import List, Any
from home_manage.models import *
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
# from app import models
# from app.models import *

# 作图
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import time
import json

import home_manage
from zhiyao import settings
from . import predict, models

# 注释掉的内容为解决错误的另一种方法
# from keras.models import load_model
# import os
# import numpy as np
# from keras.preprocessing import image
# from keras.applications.imagenet_utils import preprocess_input
# import keras
#
# model=None
#
# def read_image(img_name):
#     print('imagename:'+img_name)
#     img = image.load_img(img_name, target_size=(224, 224))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = preprocess_input(x)
#     return x
#
#
#
# def predict(imagepath):
#     categories=['bad','good','green','normal','red']
#     model=None
#     if os.path.exists('app//inception_1.h5'):
#         print('predict if')
#         keras.backend.clear_session()
#         model = load_model('app//inception_1.h5')
#         print('load successful')
#
#
#     if model != None:
#         img=read_image(imagepath)
#         print('readimage successful')
#         prediction=model.predict(img)
#         result=categories[int(prediction[0][0])]
#         print(result)
#         return result
#     else:
#         print('predict else')
#         return "error"
from .models import Incubator, FixList, User, Plant, IncubatorHistory


def get_home(request):
    """
        实现首页面功能
        :param request:
        :return:
        """
    home_image = HomeImage.objects.all().order_by('-create_time')[:3]
    policy_link = Link.objects.all().filter(link_type='国家政策').order_by('-create_time')[:2]
    guide_link = Link.objects.all().filter(link_type='中草药培养指南').order_by('-create_time')[:2]
    using_link = Link.objects.all().filter(link_type='培养箱使用手册').order_by('-create_time')[:2]
    price_link = Link.objects.all().filter(link_type='草药市场行情').order_by('-create_time')[:2]
    incubator_info = IncubatorInfo.objects.all().order_by('-create_time')[:3]
    advantage = Advantage.objects.all().order_by('-time')[:4]

    info = {
        "home_image": home_image,
        "policy_link": policy_link,
        "guide_link": guide_link,
        "using_link": using_link,
        "price_link": price_link,
        "incubator_info": incubator_info,
        "advantage": advantage,
    }

    return info


def index(request):
    info = get_home(request)
    return render(request, 'index1.html', info)


# #实现用户登陆功能
def login(request):
    if request.method == 'POST':
        userphone = request.POST.get('username')
        password = request.POST.get('password')
        if userphone and password:
            userphone = userphone.strip()
            try:
                user = models.User.objects.get(phone=userphone)
                user.lastLoginTime = datetime.now()
                user.save()
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['userid'] = user.user_id
                    request.session['userphone'] = user.phone
                    request.session['username'] = user.name
                    request.session['useremail'] = user.mail

                    request.session['userimg'] = str(user.img)
                    # request.session['userbirthday'] = user.birthday
                    request.session['userintroduction'] = user.signature
                    request.session['usersex'] = user.gender
                    # get是获取单个对象，filte是设置筛选条件
                    incubators = models.Incubator.objects.filter(user_id=userphone)
                    incuID = []
                    incu = []
                    for item in incubators:
                        incuID.append(item.incubator_id)
                        incu = zip(incuID)
                    print('login success')
                    dic = {"incu": incu}
                    info = get_home(request)
                    info.update(dic)
                    return render(request, 'index1.html', info)
                else:
                    message = '密码错误'
                    return render(request, 'signin.html', {'message': message})
            except:
                message = '用户不存在'
                return render(request, 'signin.html', {'message': message})
    return render(request, 'signin.html')


# 用户注册
def register(request):
    if request.method == 'POST':
        userphone = request.POST.get('userphone')
        password = request.POST.get('password')
        usermail = request.POST.get('usermail')
        username = request.POST.get("username")
        try:
            user = models.User.objects.get(userphonenum=userphone)
            message = '此用户已存在'
            return render(request, '../temp/register.html', {'message': message})
        except:
            try:
                user = models.User.objects.get(usermail=usermail)
                message = '此邮箱已被注册'
                return render(request, '../temp/register.html', {'message': message})
            except:
                try:
                    user = models.User.objects.get(username=username)
                    message = '此用户名已被注册'
                    return render(request, '../temp/register.html', {'message': message})
                except:
                    # userid和userphone是一样的
                    newUser = models.User()
                    newUser.userid = userphone
                    newUser.userphonenum = userphone
                    newUser.username = username
                    newUser.usermail = usermail
                    newUser.password = password
                    newUser.registration_date = datetime.now()
                    newUser.save()
                    return redirect('/login/')
    return render(request, '../temp/register.html')


# 用户登录
def signin(request):
    return render(request, 'signin.html')


# 用户注册
def signup(request):
    if request.method == 'POST':
        userphone = request.POST.get('userphone')
        password = request.POST.get('password')
        usermail = request.POST.get('usermail')
        username = request.POST.get("username")
        try:
            user = models.User.objects.get(phone=userphone)
            message = '此用户已存在'
            return render(request, 'signup.html', {'message': message})
        except:
            try:
                user = models.User.objects.get(mail=usermail)
                message = '此邮箱已被注册'
                return render(request, 'signup.html', {'message': message})
            except:
                try:
                    user = models.User.objects.get(name=username)
                    message = '此用户名已被注册'
                    return render(request, 'signup.html', {'message': message})
                except:
                    # userid和userphone是一样的
                    newUser = models.User()
                    newUser.user_id = userphone
                    newUser.phone = userphone
                    newUser.name = username
                    newUser.mail = usermail
                    newUser.password = password
                    newUser.registration_date = datetime.now()
                    newUser.save()
                    return redirect('/signin')
    return render(request, 'signup.html')


def logout(request):
    request.session.clear();
    return redirect('/')


# 通过用户id也就是手机号获取用户所有正在使用的培养箱
def getIncubator(userid):
    incubators = models.Incubator.objects.get(user_userid=userid)
    return incubators
    # 获取用户所有正在使用的培养箱


def get_incubator_info(request):
    plant_list = models.Plant.objects.all().order_by('mark')[:8]
    userphone = request.session['userphone']
    # get是获取单个对象，filte是设置筛选条件
    incubators = models.Incubator.objects.filter(user=userphone).filter(state=True)
    incuID = []
    incu = []
    plant = []
    for item in incubators:
        incuID.append(item.incubator_id)
        p = models.IncubatorHistory.objects.filter(incubator=item.incubator_id).order_by('-curTime')
        if p:
            incubator_plant = p[0].plant
        else:
            incubator_plant = '未知'
        plant.append(incubator_plant)
        incu = zip(incuID, plant)
    print('jump to incubator success')
    content = my_apply(request)
    info = {
        'plant_list': plant_list,
        'incu': incu,
    }
    info.update(content)

    return info


def incubator(request):
    info = get_incubator_info(request)
    return render(request, 'incubator.html',
                  {"incu": info['incu'], 'popular_plant': info['plant_list'], 'order': info['order']})


def getAdvice(category):
    # categories=['bad','good','green','normal','red']
    humidity = {'bad': 46.42, 'good': 46.42, 'green': 46.42, 'normal': 46.42, 'red': 46.42}
    temperature = {'bad': 25.46, 'good': 25.46, 'green': 25.46, 'normal': 25.46, 'red': 25.46}
    pressure = {'bad': 104375, 'good': 104375, 'green': 104375, 'normal': 104375, 'red': 104375}
    light = {'bad': 55231, 'good': 55231, 'green': 55231, 'normal': 55231, 'red': 55231}
    state = {'bad': '糟糕', 'good': '很好', 'green': '幼苗', 'normal': '正常状态', 'red': '营养过剩'}
    if category == 'error':
        print('读取图片存在错误，无法判断类别')
        return {"state": '暂无建议', "adviceHumidity": '暂无建议', "adviceTemperature": '暂无建议',
                "advicepressure": '暂无建议', "adviceLight": '暂无建议'}
    else:
        return {"state": state[category], "adviceHumidity": humidity[category],
                "adviceTemperature": temperature[category], "advicepressure": pressure[category],
                "adviceLight": light[category]}


# 查看培养箱的详细信息
def incubatorDeatil(request, incubatorno):
    # 这个incubatorno传递进来的是培养箱的编号
    # 需要再调用方法找到现在正在使用的培养箱的编号
    # 此处需要从培养箱的首页传递要查看培养箱的id
    # 此处假设获得，使用数据库中的 incubatorusing的id为i0101
    # iuno='i0101'

    print("pie" + incubatorno)
    ino = incubatorno
    # ino = Incubatorusing.objects.filter(incubator_incuno=incubatorno)
    # initalInfo = getInital(ino)
    # monitorInfo = getCurrent(ino)
    # iuno = getIncubatorusingID(ino)

    # 将当前用户访问的培养箱的信息存放再session中
    # request.session['incubatorid'] = iuno
    # session中的inid用于之后的页面重定向
    request.session['inid'] = ino
    request.session['true'] = True
    # 将包含初始信息和当前监控信息的两个字典合并起来
    info = {}
    incubator_id = {"incu_id": ino}
    info.update(incubator_id)

    # 处理监控信息
    monitor_data = models.IncubatorHistory.objects.filter(incubator=incubatorno).order_by('-curTime')
    # iuno = incubatorsUsing[len(incubatorsUsing) - 1].iuno  # 获取这个培养箱的使用编号的最新的那个编号
    # print(iuno)
    # monitorDatas = models.Monitorinform.objects.filter(incubatorusing_iuno=iuno).order_by('mtime')
    # monitorDatas = models.Monitorinform.objects.all().order_by('-mtime')
    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(monitor_data)

    # 获取植物相关信息
    incubator_using = monitor_data[0]
    print(incubator_using)
    plant = incubator_using.plant
    print(plant)
    plant_name = {'plant_name': plant}
    info.update(plant_name)

    # 获取建议信息
    suggest = models.Advice.objects.filter(incubator_id=incubatorno).order_by('-time')
    suggest = list(suggest)[0]
    print(suggest)
    suggest_info = {'suggest': suggest}
    info.update(suggest_info)

    # 获取传感器信息
    sensor_list = models.Sensor.objects.filter(incubator_id=incubatorno)
    sensor_list = list(sensor_list)
    print(sensor_list)
    sensor_info = {'sensor': sensor_list}
    info.update(sensor_info)

    # 获取硬件信息
    device_list = models.Device.objects.filter(incubator_id=incubatorno)
    device_list = list(device_list)
    device_info = {'device': device_list}
    info.update(device_info)

    # 获取历史数据
    old_info = get_old_info(incubatorno)
    info.update(old_info)

    time = []
    temperature = []
    humidity = []
    pressure = []
    lightIntensity = []
    monitor_data = list(monitor_data)  # 保证监控数据为list格式
    for data in monitor_data:
        time.append(str(data.curTime)[:16])
        temperature.append(data.temperature)
        humidity.append(data.humidity)
        pressure.append(data.pressure)
        lightIntensity.append(data.light)
    incubator_history = {"Mtimes": json.dumps(time[:10]), "Mtemperatures": temperature[:10],
                         "Mhumiditys": humidity[:10],
                         "Mpressures": pressure[:10], "MlightIntensitys": lightIntensity[:10], "MisSucceed": True,
                         "IisSucceed": True, }
    print(time)
    # print(monitorDatas)
    info.update(incubator_history)

    # dir = 'static/realtime_images'
    # lists = os.listdir(dir)  # 列出目录的下所有文件和文件夹保存到lists
    # print(lists)
    # lists.sort(key=lambda fn: os.path.getmtime(dir + "/" + fn), reverse=True)  # 按时间排序
    # print(lists)
    # # file_new = os.path.join(dir, lists[0])  # 获取最新的文件保存到file_new
    # file_new = dir + "/" + str(lists[0])
    # img = {'plant_image': file_new}
    url = "static/" + str(monitor_data[0].image)
    # f = open(url, 'rb')
    # data = f.read()
    # f.close()
    img = {'plant_image': url}

    info.update(img)
    # print(file_new)

    # category = predict(file_new)
    # adviceData = getAdvice(category)
    # adviceData的内容为：{"state":state,"adviceHumidity":humidity[category],"adviceTemperature":temperature[category],"advicepressure":pressure[category],"adviceLight":light[category]}
    # info.update(adviceData)
    print(info)

    return render(request, "incubator_details.html", info)


# 获取监控信息返回给调用函数
def getMointorData(incubatorno):
    incubatorsUsing = models.Incubatorusing.objects.filter(incubator_incuno=incubatorno).order_by('initializetime')
    iuno = incubatorsUsing[len(incubatorsUsing) - 1].iuno  # 获取这个培养箱的使用编号的最新的那个编号
    print(iuno)
    monitorDatas = models.Monitorinform.objects.filter(incubatorusing_iuno=iuno)


# 辅助的功能函数 将两个字典合并
def combineDict(dic1, dic2):
    info = {}
    return combineDict(dic1, dic2)


# 通过培养箱的id获得当前正在使用的这个incubatorusing的id
def getIncubatorusingID(iuno):
    inusing = models.Incubatorusing.objects.filter(incubator_incuno=iuno).last()
    # 这里需要注意的是，django里的外键是对象，不只是id
    return inusing.iuno


# 获取培养箱的初始信息，并在页面种显示出来
def getInital(ino):
    iuno = getIncubatorusingID(ino)
    # 传入的是培养箱的id
    # 这里需要使用的是incubatorusing的id
    try:
        # 获取培养箱的初始信息
        incubatorUsing = models.Incubatorusing.objects.get(iuno=iuno)
        # print(incubatorUsing.itemperature)
        # 很气人啊，在model里面，所有的id都会变成小写
        item = incubatorUsing.itemperature
        ihum = incubatorUsing.ihumidity
        ipre = incubatorUsing.ipressure
        ilig = incubatorUsing.ilightlntensity
        plant_name = incubatorUsing.plant_plantname
        info = {"Itemperature": item, "Ihumidity": ihum, "Ipressure": ipre, "IlightIntensity": ilig,
                "plant_name": plant_name, "IisSucceed": True}
        return info
    except:
        info = {"IisSucceed": True}
        return info


# 获得培养箱内的最新监控信息
def getCurrent(ino):
    iuno = getIncubatorusingID(ino)
    try:
        monitorInfo = models.Monitorinform.objects.filter(incubatorusing_iuno=iuno).order_by("mtime").last()
        mtem = monitorInfo.mtemperature
        mhum = monitorInfo.mhumidity
        mpre = monitorInfo.mpressure
        mlig = monitorInfo.mlightlntensity
        info = {"Mtemperature": mtem, "Mhumidity": mhum, "Mpressure": mpre, "MlightIntensity": mlig, "MisSucceed": True}
        return info
    except:
        info = {"MisSucceed": True}
        return info


# 由正在使用的培养箱的id获得培养箱本身的id
def getIncubatorID(iuno):
    try:
        Incubatorusing = models.Incubatorusing.objects.get(iuno=iuno)
        inno = Incubatorusing.incubator_incuno
        return inno
    except:
        print("寻找培养箱时发生错误")
    return 0


# 修改培养箱的环境信息
def alterenviroment(request, incubatorno):
    global url
    print("jingruhanshu")
    if request.method == "POST":
        light = request.POST.get('led_ctl')
        temperature = request.POST.get("tem_ctl")
        humidity = request.POST.get("hum_ctl")
        pressure = request.POST.get("pre_ctl")
        incubator_id = incubatorno

        alter_info = models.Control()
        alter_info.incubator_id = incubator_id
        alter_info.light = light
        alter_info.temperature = temperature
        alter_info.humidity = humidity
        alter_info.pres = pressure
        alter_info.save()

        url = "/incubatorDetail/" + incubator_id + "/"
    return redirect(url)


def backendlogin(request):
    return render(request, 'backendlogin.html')


def backend(request):
    #    adminstrator=request[]
    incubators = Incubator.objects.all()
    plants = Plant.objects.all()
    fixs = FixList.objects.all()
    # order = Sellpost.objects.all()
    users = User.objects.all()
    context = {
        'incubators': incubators,
        'plants': plants,
        'fixs': fixs,
        'users': users,
    }
    return render(request, 'Backend.html', context)


def get_old_info(incubatorno):
    history = models.IncubatorHistory.objects.filter(incubator=incubatorno).order_by("-"
                                                                                     "curTime")[:20]
    for data in history:
        data.curTime = data.curTime.strftime("%Y/%m/%d %H:%M:%S")
    time = []
    light = []
    temperature = []
    humility = []
    pressure = []
    plant = []
    data_list = list(history)
    for item in data_list:
        time.append(str(item.curTime)[:16])
        light.append(item.light)
        temperature.append(item.temperature)
        humility.append(item.humidity)
        pressure.append(item.pressure)
        plant.append(item.plant)
    content = {
        'history': history,
        'time': json.dumps(time),
        'temperature': json.dumps(temperature),
        'light': json.dumps(light),
        'pressure': json.dumps(pressure),
        'humidity': json.dumps(humility),
        'plant': json.dumps(plant)
    }

    return content


def plantinf_old(request, incubatorno):
    content = get_old_info(incubatorno)
    return render(request, 'old_plant_info.html', content)


def howtoplant(request):
    return render(request, 'how_to_plant.html')


def contact(request):
    return render(request, 'contact.html')


def showplant(request, pindex):
    plant_list = []
    if request.method == "POST":
        button_list = request.POST.get("choice")
        print(button_list)
        search = request.POST.get("search")
        if search != '':
            if "k1" == button_list:
                plant_list = models.Plant.objects.filter(name__icontains=search).filter(isShow='是').order_by('time')
            elif "k2" == button_list:
                plant_list = models.Plant.objects.filter(name__icontains=search).filter(isShow='是').order_by('mark')
            elif "k3" == button_list:
                plant_list = models.Plant.objects.filter(name__icontains=search).filter(isShow='是').order_by(
                    'plant_type')
        else:
            if "k1" == button_list:
                plant_list = models.Plant.objects.filter(isShow='是').order_by('-time')
            elif "k2" == button_list:
                plant_list = models.Plant.objects.filter(isShow='是').order_by('-mark')
            elif "k3" == button_list:
                plant_list = models.Plant.objects.filter(isShow='是').order_by('name')
    else:
        plant_list = models.Plant.objects.filter(isShow='是').order_by('-time')
    # 分页
    print(plant_list)
    paginator = Paginator(plant_list, 6)  # 实例化Paginator, 每页显示5条数据
    if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
        pindex = 1
    else:  # 如果有返回在值，把返回值转为整数型
        int(pindex)
    page = paginator.page(pindex)  # 传递当前页的实例对象到前端

    popular_plant = models.Plant.objects.all().order_by('-popularity')[:15]

    content = {
        'plant_list': plant_list,
        'popular_plant': popular_plant,
        "page": page
    }
    return render(request, 'show_plant.html', content)


def plantdetail(request, id):
    plant = models.Plant.objects.get(id=id)
    plant_info = models.PlantDetail.objects.get(plant_id=id)
    plant.popularity = plant.popularity + 1
    print(plant.popularity)
    content = {
        "plantInfo": plant_info,
        "plant": plant
    }
    return render(request, 'plant_detail.html', content)


def submit_plant_judge(request):
    is_success = 'False'
    if request.method == 'POST':
        name = request.POST.get('pName')
        place = request.POST.get('pPlace')
        effect = request.POST.get('pEffect')
        taboo = request.POST.get('pTaboo')
        shape = request.POST.get('pShape')
        phone = request.POST.get('pPhone')
        img = request.FILES.get('pImg')
        try:
            if name and place and effect and taboo and shape and phone and img:
                plant = models.Plant()
                plant_detail = models.PlantDetail()
                incubator_id = models.Incubator.objects.get(incubator_id='i01')

                plant.name = name
                plant.img = img
                plant.mark = 80
                plant.incubator = incubator_id
                plant.save()

                plant_detail.plant_name = name
                plant_detail.effect = effect
                plant_detail.place = place
                plant_detail.shape = shape
                plant_detail.taboo = taboo
                plant_detail.plant_id = plant
                plant_detail.save()
                is_success = 'True'
                return is_success
        except:
            pass
    return is_success


def submitPlant(request):
    is_success = submit_plant_judge(request)
    # request.session['is_success'] = is_success
    if is_success == 'False':
        return redirect('/publishPlant/')
    return redirect('/showplant/1')


def bbs(request):
    return render(request, 'bbs.html')


def my(request):
    userphone = request.session['userphone']
    # get是获取单个对象，filte是设置筛选条件
    incubators = models.Incubator.objects.filter(user_userid=userphone)
    incuName = []
    incuID = []
    incu = []
    for item in incubators:
        incuName.append(item.incuname)
        incuID.append(item.incuno)
        incu = zip(incuName, incuID)
    print('jump to incubator success')
    return render(request, 'my.html', {"incu": incu})
    # return render(request,'my.html')


def showplant1(request, pindex):
    plant_list = []
    if request.method == "POST":
        button_list = request.POST.get("choice")
        print(button_list)
        search = request.POST.get("search")
        if search != '':
            if "k1" == button_list:
                plant_list = models.Plant.objects.filter(name__icontains=search).filter(isShow='是').order_by('time')
            elif "k2" == button_list:
                plant_list = models.Plant.objects.filter(name__icontains=search).filter(isShow='是').order_by('mark')
            elif "k3" == button_list:
                plant_list = models.Plant.objects.filter(name__icontains=search).filter(isShow='是').order_by(
                    'plant_type')
        else:
            if "k1" == button_list:
                plant_list = models.Plant.objects.filter(isShow='是').order_by('-time')
            elif "k2" == button_list:
                plant_list = models.Plant.objects.filter(isShow='是').order_by('-mark')
            elif "k3" == button_list:
                plant_list = models.Plant.objects.filter(isShow='是').order_by('name')
    else:
        plant_list = models.Plant.objects.filter(isShow='是').order_by('-time')
    # 分页
    print(plant_list)
    paginator = Paginator(plant_list, 6)  # 实例化Paginator, 每页显示5条数据
    if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
        pindex = 1
    else:  # 如果有返回在值，把返回值转为整数型
        int(pindex)
    page = paginator.page(pindex)  # 传递当前页的实例对象到前端

    popular_plant = models.Plant.objects.all().order_by('-popularity')[:15]

    content = {
        'plant_list': plant_list,
        'popular_plant': popular_plant,
        "page": page
    }
    return render(request, 'show_plant.html', content)


def get_link(request):
    link = []
    if request.method == "POST":
        button_list = request.POST.get("choice")
        # print(button_list)
        search = request.POST.get("search")
        print(search)
        if search != '':
            if "k1" == button_list:
                link = Link.objects.filter(link_title__icontains=search).filter(link_type='国家政策').order_by(
                    '-create_time')
            elif "k2" == button_list:
                link = Link.objects.filter(link_title__icontains=search).filter(link_type='中草药培养指南').order_by(
                    '-create_time')
            elif "k3" == button_list:
                link = Link.objects.filter(link_title__icontains=search).filter(link_type='培养箱使用手册').order_by(
                    '-create_time')
            elif "k4" == button_list:
                link = Link.objects.filter(link_title__icontains=search).filter(link_type='草药市场行情').order_by(
                    '-create_time')
        else:
            if "k1" == button_list:
                link = Link.objects.filter(link_type='国家政策').order_by('-create_time')
            elif "k2" == button_list:
                link = Link.objects.filter(link_type='中草药培养指南').order_by('-create_time')
            elif "k3" == button_list:
                link = Link.objects.filter(link_type='培养箱使用手册').order_by('-create_time')
            elif "k4" == button_list:
                link = Link.objects.filter(link_type='草药市场行情').order_by('-create_time')
    else:
        link = Link.objects.all().order_by('-create_time')
    time_list = []
    # 分页
    print(link)
    return link


def more(request,pindex):
    # link = Link.objects.all()
    link = get_link(request)
    paginator = Paginator(link, 6)  # 实例化Paginator, 每页显示5条数据
    if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
        pindex = 1
    else:  # 如果有返回在值，把返回值转为整数型
        int(pindex)
    page = paginator.page(pindex)  # 传递当前页的实例对象到前端
    content = {
        'link': link,
        "page": page
    }
    return render(request, 'more.html', content)


def writePurchase(request):
    return render(request, 'writePurchase.html')


def publishPlant(request):
    return render(request, "publish_plant.html")


def writeCommunication(request):
    return render(request, "writeCommunication.html")


def savePurchase(request, userphone):
    if request.method == 'POST':
        pid = str(userphone) + str(time.time())
        pMedicine = request.POST.get('pMedicine')
        pPrice = request.POST.get("pPrice")
        pDescribe = request.POST.get("pDescribe")
        pPhone = request.POST.get("pPhone")

        newBuy = models.Buypost()
        newBuy.bid = pid
        newBuy.bplant = pMedicine
        newBuy.bprice = pPrice
        newBuy.bdescription = pDescribe
        newBuy.bphonenum = pPhone
        usr = models.User.objects.get(userid=userphone)
        newBuy.user_userid = usr
        newBuy.save()
    return redirect("/bbs/")


def saveSelling(request, userphone):
    return redirect('/bbs/')


def saveCommunication(request, userphone):
    return redirect('/bbs/')


def getPurchase(request):
    print("尝试成功")
    # return HttpResponse('执行成功')
    return render(request, '../temp2/../temp/bbs.html')


def getSelling(request):
    return HttpResponse("selling")


def getAll(request):
    return HttpResponse('all')


def getMy():
    pass


def getbbs(request):
    # 把所有的信息都展示出来
    clist = models.Commentpost.objects.all().order_by('-releasectime')
    slist = models.Sellpost.objects.all().order_by('-releasestime')
    plist = models.Buypost.objects.all().order_by('-releasebtime')
    return render(request, '../temp2/../temp/bbs.html', {'clist': clist, 'slist': slist, 'plist': plist})


# 购买
def getPDetail(request, id):
    try:
        purchase = models.Buypost.objects.get(bid=id)
        return render(request, 'purchaseDetail.html', {"pDetail": purchase, 'success': True})
    except:
        return render(request, '../temp2/../temp/bbs.html', {'success': False})


def getSDetail(request, id):
    try:
        selling = models.Sellpost.objects.get(sid=id)
        return render(request, 'sellingDetail.html', {'sDetail': selling, 'success': True})
    except:
        return render(request, '../temp2/../temp/bbs.html', {'success': False})


def getCDetail(request, id):
    try:
        communication = models.Commentpost.objects.get(cid=id)
        return render(request, 'communicationDetail.html', {'cDetail': communication, 'success': True})
    except:
        print('meizhaodao')
        return render(request, '../temp2/../temp/bbs.html', {'success': False})


# #########################################################################################################
# # 以下是有关硬件的请求处理代码
# #########################################################################################################
# from django.shortcuts import render
# from app.models import ChangeLog
# from app.models import ViewParam
# from django.http import HttpResponse
# import os
# # 1.处理来自 硬件的请求
# # 在ViewLog中添加一条环境参数，查看并返回最新的一条ChangeLog表的记录
# # 2.返回一张最新的监控图片
# # 3.网页上来自用户的修改记录被存库，并返回箱子的实时数据

# # 1.
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def proHard(request):
#     request.encode = "utf-8"
#     response = ''
#     clg = ChangeLog.objects.all().order_by("-addtime")
#     clg = clg[0]
#     tem_ctl = clg.tem
#     hum_ctl = clg.hum
#     pre_ctl = clg.pre
#     led_ctl = clg.led
#     tem_ctl_need = 5 - len(tem_ctl)
#     hum_ctl_need = 5 - len(hum_ctl)
#     led_ctl_need = 5 - len(led_ctl)
#     pre_ctl_need = 6 - len(pre_ctl)
#     a = "0"
#     for i in range(tem_ctl_need):
#         tem_ctl = a + tem_ctl
#     for i in range(led_ctl_need):
#         led_ctl = a + led_ctl
#     for i in range(pre_ctl_need):
#         pre_ctl = a + pre_ctl
#     for i in range(hum_ctl_need):
#         hum_ctl = a + hum_ctl
#     response += 't=' + tem_ctl + '&' + 'l=' + led_ctl + '&p=' + pre_ctl + '&h=' + hum_ctl
#     # response+='_*_'+'t='+tem_ctl+'&'+'l='+led_ctl+'&p='+pre_ctl+'&h='+hum_ctl
#     print(request)
#     if request.method == 'POST':
#         txt = request.POST['text']
#         print("get text:", txt)
#         # 处理文本数据并存库
#         param_split = txt.split('&')
#         param_t = param_split[0].split('=')[1]
#         param_l = param_split[1].split('=')[1]
#         param_p = param_split[2].split('=')[1]
#         param_h = param_split[3].split('=')[1]

#         mif = Monitorinform()
#         mif.mpressure = param_p
#         mif.mtemperature = param_t
#         mif.mlightlntensity = param_l
#         mif.mhumidity = param_h
#         mif.mplantstage = 1
#         mif.save()

#         vpm = ViewParam()
#         vpm.tem = param_t
#         vpm.led = param_l
#         vpm.pre = param_p
#         vpm.hum = param_h
#         vpm.save()

#     return HttpResponse(response)


# # 2.
# def returnImage(request):
#     dir = 'realtime_images'
#     lists = os.listdir(dir)  # 列出目录的下所有文件和文件夹保存到lists
#     # print(lists)
#     lists.sort(key=lambda fn: os.path.getmtime(dir + "/" + fn))  # 按时间排序
#     file_new = os.path.join(dir, lists[-1])  # 获取最新的文件保存到file_new
#     # print(file_new)
#     f = open(file_new, 'rb')
#     data = f.read()
#     f.close()
#     return HttpResponse(data, content_type="image/jpeg")


# # 3.
# def proIncubator2(request):
#     res = {}  # 存储箱子的相关信息
#     # 取出最早的一条数据
#     Obj = ViewParam.objects.all().order_by('-addtime')
#     if Obj:
#         Obj = Obj[0]
#         res['pressure'] = Obj.pre
#         res['light'] = Obj.led
#     else:
#         pass
#     # 事实上这些生成图像的代码应该放到处理硬件的视图中
#     vplist = ViewParam.objects.all()
#     timelist = []
#     temperaturelist = []
#     humiditylist = []
#     pressurelist = []
#     lightlist = []
#     for vp in vplist:
#         timelist.append(vp.addtime)
#         temperaturelist.append(vp.tem)
#         humiditylist.append(vp.hum)
#         pressurelist.append(vp.pre)
#         lightlist.append(vp.led)
#     dir = 'media'
#     file = os.path.join(dir, "humidityChart.jpg")  # 图片要保存到的位置
#     graph(timelist, humiditylist, file)
#     file = os.path.join(dir, "temperatureChart.jpg")  # 图片要保存到的位置
#     graph(timelist, temperaturelist, file)
#     file = os.path.join(dir, "pressureChart.jpg")  # 图片要保存到的位置
#     graph(timelist, pressurelist, file)
#     file = os.path.join(dir, "lightChart.jpg")  # 图片要保存到的位置
#     graph(timelist, lightlist, file)

#     if request.POST:
#         clg = ChangeLog()
#         clg.tem = request.POST['tem_ctl']
#         clg.hum = request.POST['hum_ctl']
#         clg.led = request.POST['led_ctl']
#         clg.pre = request.POST['pre_ctl']
#         clg.save()
#         res['response'] = "修改已经收到：" + clg.tem
#     return render(request, 'incubatorDetail2.html', res)


# # 4.
# def proIncubator(request, incubatorno):
#     if request.POST:
#         print("开始处理++++++++++++++++++++++++++++++++++++++++++")
#         clg = ChangeLog()
#         clg.tem = request.POST['tem_ctl']
#         clg.hum = request.POST['hum_ctl']
#         clg.led = request.POST['led_ctl']
#         clg.pre = request.POST['pre_ctl']

#         clg.save()

#         incubator = Incubatorusing.objects.get(iuno=incubatorno)

#         ino1 = incubator.incubator_incuno.incuno
#         ino = (ino1,)
#     return HttpResponseRedirect(reverse('incubatorDetail', args=ino))


# # 用户初次使用系统流程
# def guide(request):
#     return render(request, 'connectingGuide.html')


# # 作图：

# def graph(x, y, file):
#     # y = [0.236, 0.256, 0.288, 0.483, 0.621, 0.737, 0.796, 0.845, 0.833, 0.802]
#     # x = [20, 30, 40, 80, 150, 250, 350, 400, 450, 500]
#     fig = plt.figure()
#     ax1 = fig.add_subplot(1, 1, 1, facecolor='white')
#     ax1.set_xlabel('时间')  # 设置x轴名称
#     ax1.set_ylabel('值')  # 设置y轴名称
#     # 设置y轴坐标范围
#     plt.title("Figure1_GrayLevel&F1core")

#     ax1.yaxis.grid(True, which='minor')
#     ax1.plot(x, y, marker='v', color='k', label='fun1', linestyle='dashed')
#     plt.savefig(file)


# # 用作测试
# def test(request):
#     return render(request, 'test.html')


def updateUserInfo(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        user = models.User.objects.get(user_id=userid)
        user.gender = request.POST.get('usersex')
        user.signature = request.POST.get('userintroduction')
        user.phone = request.POST.get('userphone')
        user.user_id = request.POST.get('userphone')
        user.mail = request.POST.get('useremail')
        # user.birthday = request.POST.get('userbirthday')
        user.name = request.POST.get('username')
        img = request.FILES.get('pImg', None)
        if img:
            user.img = str(img).lstrip("/static/img/personInfo")
        else:
            user.img = 'avator.jpg'
        user.save()
        request.session['userid'] = user.user_id
        request.session['userphone'] = user.phone
        request.session['username'] = user.name
        request.session['userimg'] = user.img
        request.session['useremail'] = user.mail
        request.session['userintroduction'] = user.signature
        request.session['usersex'] = user.gender
        print(user)
    return redirect('/incubator/')


def referfix(request, incubatorno):
    fix_url = "/incubatorDetail/" + incubatorno + "/"
    fixDescribe = request.POST.get('fixDescribe')
    fixPhone = request.POST.get('fixPhone')
    fixAddress = request.POST.get('fixAddress')
    fix_info = models.FixList()
    incubator_fix = models.Incubator.objects.get(incubator_id=incubatorno)
    fix_info.incubator_id = incubator_fix
    fix_info.time = datetime.now()
    fix_info.phone = fixPhone
    fix_info.describe = fixDescribe
    fix_info.address = fixAddress
    fix_info.save()
    time.sleep(3)
    return redirect(fix_url)


def verify_connect(request):
    if request.method == 'POST':
        incubator_id = request.POST.get('incubator_id')
        key = request.POST.get('key')
        print(incubator_id)
        print(key)
        result = 'Fail'
        if incubator_id and key:
            try:
                incubator = models.Incubator.objects.get(incubator_id=incubator_id)
                if incubator and incubator.key == key:
                    result = "Success"
                    incubator.state = True
                    incubator.save()
                    return result
            except:
                return result
    return result


def connect(request):
    isSuccess = verify_connect(request)
    print(isSuccess)
    # result_key = request.session.result
    # if result_key:
    #     request.session.delete(result_key)
    request.session['result'] = ''
    if request.session['result']:
        del request.session['result']
    request.session['result'] = isSuccess
    time.sleep(3)
    return redirect("/incubator/")


def connect1(request):
    if request.method == 'POST':
        incubator_id = request.POST.get('incubator_id')
        key = request.POST.get('key')
        if incubator_id and key:
            try:
                incubator = models.Incubator.objects.get(incubator_id=incubator_id)
                incubator.state = True
                incubator.save()
                time.sleep(5)
                return redirect('/incubator/')
            except:
                time.sleep(5)
                return redirect('/incubator/')
    time.sleep(5)
    return redirect('/incubator/')


def disconnected(request, incubatorno):
    incubator = models.Incubator.objects.get(incubator_id=incubatorno)
    incubator.state = False
    incubator.save()
    time.sleep(3)
    return redirect('/incubator/')


def insert(request):
    tem = request.POST.get('PsTem')
    hum = request.POST.get('PsHum')
    press = request.POST.get('PsPress')
    light = request.POST.get('PsLight')
    incu_id = request.POST.get('BoxId')
    plant = request.POST.get('Plant')
    print(tem)
    print(hum)
    print(press)
    print(light)

    time = datetime.now()
    print(time)
    data = models.IncubatorHistory()
    data.curTime = time
    data.temperature = tem
    data.humidity = hum
    incu = models.Incubator.objects.filter(incubator_id=incu_id)
    data.incubator = incu[0]
    data.pressure = press
    data.light = light
    data.plant = plant
    print(data)
    data.save()
    return HttpResponse("success")


# def plant(request):
#     plant_list = models.Plant.objects.all()
#     print(list)
#     page = request.GET.get('page')
#     paginator = Paginator(list, 3)
#     try:
#         plant_list = paginator.page(page)
#     except PageNotAnInteger:
#         plant_list = paginator.page(1)
#     except EmptyPage:
#         plant_list = paginator.page(paginator.num_pages)
#     return render(request, 'show_plant.html', locals())


def monitor(request):
    data = models.IncubatorHistory()
    data.pressure = json.loads(request.body).get("y")
    data.temperature = json.loads(request.body).get("w")
    data.light = json.loads(request.body).get("g")
    data.humidity = json.loads(request.body).get("s")
    incubator_id = json.loads(request.body).get('id')
    incubator_id = 'i0' + str(incubator_id)
    print(incubator_id)
    print(data.temperature)
    print(data.humidity)
    incu = models.Incubator.objects.filter(incubator_id=incubator_id)
    print(incu)
    data.incubator = incu[0]

    image = base64.b64decode(json.loads(request.body).get("img"))
    filename = time.strftime('%Y%m%d%H%M%S', time.localtime())
    filename += '.jpeg'
    f = open('static/realtime_images/' + filename, 'wb')
    f.write(image)
    f.close()

    data.image = 'realtime_images/' + filename
    print(json.loads(request.body).get("img"))
    data.save()

    try:
        control = models.Control.objects.filter(incubator_id=data.incubator).order_by('-time')[0]
        response = {
            'w': control.temperature,
            's': control.humidity,
            'g': control.light,
            'y': control.pres,
        }
        print(2)
    except:
        response = {
            'w': 15,
            's': 40,
            'g': 4000,
            'y': 101,
        }
        print(1)
    return HttpResponse(json.dumps(response))


def hardcontrol(request):
    control = models.Control()
    incubator_id = json.loads(request.body).get('id')
    incu = 'i0' + str(incubator_id)
    control.incubator_id = incu
    # incu = models.Incubator.objects.filter(incubator_id=incubator_id)
    # control.incubator = incu[0]
    control.humidity = json.loads(request.body).get('s')
    control.temperature = json.loads(request.body).get('w')
    control.light = json.loads(request.body).get('g')
    control.pres = json.loads(request.body).get('y')
    control.save()
    con1 = models.Control.objects.filter(incubator_id=control.incubator_id).order_by('-time')[0]
    response = {
        'w': con1.temperature,
        's': con1.humidity,
        'g': con1.light,
        'y': con1.pres,
    }
    return HttpResponse(json.dumps(response))


def return_image(request):
    incubator_id = request.GET.get('iden')
    newest_img = IncubatorHistory.objects.filter(incubator_id=incubator_id).order_by('-curTime')[0]
    img_url = 'static/' \
              '' + str(newest_img.image)
    print(img_url)
    file = open(img_url, 'rb')
    img = file.read()
    file.close()
    return HttpResponse(img, content_type="image/jpg")


def newIncubator(request):
    return render(request, 'newIncubator.html')


def apply(request):
    number = request.POST.get('number')
    print(number)
    return render(request, 'apply_detail.html', {'in_number': number})


def submitApply(request):
    if request.method == 'POST':
        name = request.POST.get('iName')
        phone = request.POST.get('iPhone')
        career = request.POST.get('iCa')
        school = request.POST.get('iSchool')
        using = request.POST.get('iDist')
        sensor = request.POST.getlist('iSensor')
        # province = request.POST.get('iPro')
        # print(province)
        # print(str(province))
        # city = request.POST.get('iCity')
        # print(city)
        # area = request.POST.get('iArea')
        # print(area)
        detail_addr = request.POST.get('iDetailAddr')
        number = request.POST.get('iNumber')

        user_phone = request.session['userphone']
        user = models.User.objects.get(user_id=user_phone)
        my_incubator = models.Incubator()
        incu_id = int(random.random() * 1000000)
        my_incubator.incubator_id = 'i' + str(incu_id)
        my_incubator.schedule = '用户申请中，待通过'
        my_incubator.user = user
        my_incubator.save()

        for i in sensor:
            sensor = models.Sensor()
            sensor.sensor_name = i
            sensor.incubator_id = my_incubator
            sensor.save()

        order = models.UserOrder()
        order.addr = detail_addr
        order.using = using
        order.number = number
        order.phone = phone
        order.career = career
        order.company_or_school = school
        order.user = user
        order.save()
    time.sleep(30)
    return redirect('/incubator/')


def my_apply(request):
    user = request.session['userphone']
    order = models.UserOrder.objects.filter(user_id=user).order_by('-order_time')
    print(order)

    content = {
        'order': order,
    }
    return content


def submit_order_issue(request):
    if request.method == 'POST':
        order_issue = models.OrderIssue()
        name = request.POST.get('oName')
        email = request.POST.get('oEmail')
        phone = request.POST.get('oPhone')
        order_id = request.POST.get('order_id')
        order_describe = request.POST.get('order_describe')
        order = models.UserOrder.objects.get(id=order_id)
        print(order)
        order_issue.order = order
        order_issue.name = name
        order_issue.email = email
        order_issue.phone = phone
        order_issue.describe = order_describe
        order_issue.save()
        time.sleep(3)
    return redirect('/incubator/')


def go_order_issue(request, order_id):
    order_id = order_id
    return render(request, 'order_issue.html', {'order_id': order_id})
