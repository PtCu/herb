# Register your models here.
from django.contrib import admin

from . import models



class LightSensorInline(admin.StackedInline):
    model = models.LightSensor
    max_num = 5
    extra=0

class PressureSensorInline(admin.StackedInline):
    model = models.PressureSensor
    extra=0

class TemperatureSensorInline(admin.StackedInline):
    model = models.TemperatureSensor
    extra=0

class HumiditySensorInline(admin.StackedInline):
    model = models.HumiditySensor
    extra=0

class CameraInline(admin.StackedInline):
    model = models.Camera
    extra=0

class PlantInline(admin.StackedInline):
    model = models.Plant
    extra=0

class IncubatorHistoryInline(admin.StackedInline):
    model = models.IncubatorHistory
    extra=0

class IncubatorInline(admin.StackedInline):
    model = models.Incubator
    extra = 0
    
class IncubatorAdmin(admin.ModelAdmin):
    inlines = [LightSensorInline, PressureSensorInline, TemperatureSensorInline,
               HumiditySensorInline, CameraInline, PlantInline, IncubatorHistoryInline]
    list_display = ('incubator_id', 'incubator_type', 'state',)
    list_display_links = ('incubator_id', 'incubator_type')
    list_per_page = 50		# 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('incubator_id', 'incubator_type', 'state')
    search_fields = ('incubator_id', 'incubator_type', 'state',)  # 指定能搜索哪些字段
    #list_editable = ['incubator_type', 'state']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['incubator_id']  # 设置只读字段，不允许更改
    ordering = ('-incubator_id',)  # 定义列表显示的顺序，负号表示降序


class FixListAdmin(admin.ModelAdmin):
    fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    list_display = ('id', 'time')
    
    list_display_links = ('id', 'time')
    list_per_page = 50		# 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('id', 'time')
    search_fields = ('id', 'time')  # 指定能搜索哪些字段
  #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id']  # 设置只读字段，不允许更改
    ordering = ('-id',)  # 定义列表显示的顺序，负号表示降序

class LightSensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_type','state','start_time','data')
    fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    list_display_links = ('id', 'model_type')
    list_per_page = 50		# 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('id','model_type')
    search_fields = ('id', 'model_type')  # 指定能搜索哪些字段
  #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id','data']  # 设置只读字段，不允许更改
    ordering = ('-id',)  # 定义列表显示的顺序，负号表示降序
    

class PressureSensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_type','state','start_time','data')
    fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    list_display_links = ('id', 'model_type')
    list_per_page = 50		# 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('id', 'model_type')
    search_fields = ('id', 'model_type')  # 指定能搜索哪些字段
  #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id','data']  # 设置只读字段，不允许更改
    ordering = ('-id',)  # 定义列表显示的顺序，负号表示降序

class TemperatureSensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_type','state','start_time','data')
    fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    list_display_links = ('id', 'model_type')
    list_per_page = 50		# 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('id', 'model_type')
    search_fields = ('id', 'model_type')  # 指定能搜索哪些字段
  #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id','data']  # 设置只读字段，不允许更改
    ordering = ('-id',)  # 定义列表显示的顺序，负号表示降序

class HumiditySensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_type','state','start_time','data')
    fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    list_display_links = ('id', 'model_type')
    list_per_page = 50		# 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('id', 'model_type')
    search_fields = ('id', 'model_type')  # 指定能搜索哪些字段
  #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id','data']  # 设置只读字段，不允许更改
    ordering = ('-id',)  # 定义列表显示的顺序，负号表示降序

class CameraAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_type','state','start_time','data')
    fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    list_display_links = ('id', 'model_type')
    list_per_page = 50		# 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('id', 'model_type')
    search_fields = ('id', 'model_type')  # 指定能搜索哪些字段
  #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id','data']  # 设置只读字段，不允许更改
    ordering = ('-id',)  # 定义列表显示的顺序，负号表示降序

class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'plant_type','name','state','time','mark','popularity')
    fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    list_display_links = ('id', 'time')
    list_per_page = 50		# 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('id', 'plant_type','name','state','time','mark','popularity')
    search_fields = ('id', 'plant_type','name','state','time','mark','popularity')  # 指定能搜索哪些字段
  #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id','plant_type']  # 设置只读字段，不允许更改
    ordering = ('-id',)  # 定义列表显示的顺序，负号表示降序


class UserAdmin(admin.ModelAdmin):
    inlines = [IncubatorInline]
    list_display = ('user_id', 'phone', 'name', 'gender')
    list_display_links = ('user_id', 'phone')
    list_per_page = 50		# 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('user_id', 'phone', 'name', 'gender')
    search_fields = ('user_id', 'phone', 'name', 'gender',)  # 指定能搜索哪些字段
    list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['phone']  # 设置只读字段，不允许更改
    ordering = ('-user_id', )  # 定义列表显示的顺序，负号表示降序
    # fieldsets = (		# 对字段进行分类设置，前端会分开显示
    #     (None, {'fields': ('name', 'password', )}),
    #     ('Personal info', {'fields': ('user_id', )}),
    #     ('Permissions', {'fields': ('gender', )}),
    # )
    # add_fieldsets = (	# 定义添加数据时需要填写哪些字段
    #     (None, {'classes': ('wide',), 'fields': ('name', 'content' )}),
    #     )

class IncubatorHistoryAdmin(admin.ModelAdmin):
    list_display = ('curTime', 'light', 'pressure', 'humidity','temperature','plant')
    fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    list_display_links = ('curTime', 'light', 'pressure')
    list_per_page = 50		# 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('curTime', 'light', 'pressure', 'humidity','temperature','plant')
    search_fields = ('curTime', 'light', 'pressure', 'humidity','temperature','plant')  # 指定能搜索哪些字段
  #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['curTime', 'light', 'pressure', 'humidity','temperature','plant']  # 设置只读字段，不允许更改
    ordering = ('-curTime',)  # 定义列表显示的顺序，负号表示降序

admin.site.register(models.FixList,FixListAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Incubator,IncubatorAdmin)
admin.site.register(models.LightSensor,LightSensorAdmin)
admin.site.register(models.Plant,PlantAdmin)
admin.site.register(models.PressureSensor,PressureSensorAdmin)
admin.site.register(models.TemperatureSensor,TemperatureSensorAdmin)
admin.site.register(models.HumiditySensor,HumiditySensorAdmin)
admin.site.register(models.Camera,CameraAdmin)
admin.site.register(models.IncubatorHistory,IncubatorHistoryAdmin)
# admin.site.register(models.Administrator)


admin.site.site_header = '中草药管理系统'
admin.site.site_title = '中草药管理系统'
