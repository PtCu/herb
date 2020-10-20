# Register your models here.
from django.contrib import admin

from . import models

admin.site.register(models.User)
admin.site.register(models.Incubator)
admin.site.register(models.LightSensor)
admin.site.register(models.Plant)
admin.site.register(models.PressureSensor)
admin.site.register(models.TemperatureSensor)
admin.site.register(models.HumiditySensor)
admin.site.register(models.Camera)
admin.site.register(models.IncubatorHistory)
admin.site.register(models.Administrator)
