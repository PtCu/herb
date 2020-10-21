# Register your models here.
from django.contrib import admin

from . import models


class CameraInline(admin.StackedInline):
    model = models.Camera
    extra = 0


class DeviceInline(admin.StackedInline):
    model = models.Device
    extra = 0


class SensorInline(admin.StackedInline):
    model = models.Sensor
    extra = 0


class AdviceInline(admin.StackedInline):
    model = models.Advice


class ControlInline(admin.StackedInline):
    model = models.Control


class PlantInline(admin.StackedInline):
    model = models.Plant
    extra = 0


class IncubatorHistoryInline(admin.StackedInline):
    model = models.IncubatorHistory
    extra = 0


class IncubatorInline(admin.StackedInline):
    model = models.Incubator
    extra = 0


class IncubatorAdmin(admin.ModelAdmin):
    inlines = [CameraInline, PlantInline, IncubatorHistoryInline]
    list_display = ('incubator_id', 'user', 'incubator_type', 'state')
    list_display_links = ('incubator_id', 'incubator_type', 'user')
    list_per_page = 50  # 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('incubator_id', 'incubator_type', 'state')
    search_fields = ('incubator_id', 'incubator_type', 'state',)  # 指定能搜索哪些字段
    # list_editable = ['incubator_type', 'state']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['incubator_id']  # 设置只读字段，不允许更改
    ordering = ('incubator_id',)  # 定义列表显示的顺序，负号表示降序


class FixListAdmin(admin.ModelAdmin):
    fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    list_display = ('id','incubator_id', 'time','state')

    list_display_links = ('id', 'time')
    list_per_page = 50  # 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('id', 'time','incubator_id','state')
    search_fields = ('id', 'time','incubator_id','state')  # 指定能搜索哪些字段
    #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id', 'time','incubator_id']  # 设置只读字段，不允许更改
    ordering = ('-time',)  # 定义列表显示的顺序，负号表示降序


class CameraAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_type', 'state', 'start_time', 'data')
    fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    list_display_links = ('id', 'model_type')
    list_per_page = 50  # 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('id', 'model_type')
    search_fields = ('id', 'model_type')  # 指定能搜索哪些字段
    #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id', 'data']  # 设置只读字段，不允许更改
    ordering = ('-id',)  # 定义列表显示的顺序，负号表示降序


class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'plant_type', 'name', 'state', 'time', 'mark', 'popularity')
    fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    list_display_links = ('id', 'time')
    list_per_page = 50  # 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('id', 'plant_type', 'name', 'state', 'time', 'mark', 'popularity')
    search_fields = ('id', 'plant_type', 'name', 'state', 'time', 'mark', 'popularity')  # 指定能搜索哪些字段
    #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id', 'plant_type']  # 设置只读字段，不允许更改
    ordering = ('-id',)  # 定义列表显示的顺序，负号表示降序


class UserAdmin(admin.ModelAdmin):
    inlines = [IncubatorInline]
    list_display = ('user_id', 'phone', 'name', 'gender')
    list_display_links = ('user_id', 'phone')
    list_per_page = 50  # 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('user_id', 'phone', 'name', 'gender')
    search_fields = ('user_id', 'phone', 'name', 'gender',)  # 指定能搜索哪些字段
    list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['phone']  # 设置只读字段，不允许更改
    ordering = ('-user_id',)  # 定义列表显示的顺序，负号表示降序
    # fieldsets = (		# 对字段进行分类设置，前端会分开显示
    #     (None, {'fields': ('name', 'password', )}),
    #     ('Personal info', {'fields': ('user_id', )}),
    #     ('Permissions', {'fields': ('gender', )}),
    # )
    # add_fieldsets = (	# 定义添加数据时需要填写哪些字段
    #     (None, {'classes': ('wide',), 'fields': ('name', 'content' )}),
    #     )


class IncubatorHistoryAdmin(admin.ModelAdmin):
    list_display = ('curTime', 'light', 'pressure', 'humidity', 'temperature', 'plant')
    fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    list_display_links = ('curTime', 'light', 'pressure')
    list_per_page = 50  # 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('curTime', 'light', 'pressure', 'humidity', 'temperature', 'plant')
    search_fields = ('curTime', 'light', 'pressure', 'humidity', 'temperature', 'plant')  # 指定能搜索哪些字段
    #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['curTime', 'light', 'pressure', 'humidity', 'temperature', 'plant']  # 设置只读字段，不允许更改
    ordering = ('-curTime',)  # 定义列表显示的顺序，负号表示降序


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'incubator_id', 'device_type', 'device_name', 'device_state', 'delivery_time', 'service_life')
    # fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    # list_display_links = ('curTime', 'light', 'pressure')
    list_per_page = 50  # 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('device_type', 'device_name', 'device_state')
    search_fields = ('device_type', 'device_name', 'device_state')  # 指定能搜索哪些字段
    #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id', 'incubator_id', 'device_type', 'device_name', 'delivery_time',
                       'service_life']  # 设置只读字段，不允许更改
    ordering = ('-incubator_id',)  # 定义列表显示的顺序，负号表示降序


class ControlAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'humidity', 'temperature', 'light', 'pres', 'incubator_id')
    # fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    # list_display_links = ('curTime', 'light', 'pressure')
    list_per_page = 50  # 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('time', 'incubator_id')
    search_fields = ('time', 'incubator_id')  # 指定能搜索哪些字段
    #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id', 'time', 'humidity', 'temperature', 'light', 'pres', 'incubator_id']  # 设置只读字段，不允许更改
    ordering = ('-time',)  # 定义列表显示的顺序，负号表示降序


class SensorAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'incubator_id', 'sensor_type', 'sensor_name', 'sensor_state', 'delivery_time', 'service_life',
        'sensor_value')
    # fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    # list_display_links = ('curTime', 'light', 'pressure')
    list_per_page = 50  # 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('incubator_id', 'sensor_type', 'sensor_name', 'sensor_state')
    search_fields = ('incubator_id', 'sensor_type', 'sensor_name', 'sensor_state')  # 指定能搜索哪些字段
    #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id', 'incubator_id', 'sensor_type', 'sensor_name', 'delivery_time', 'service_life',
                       'sensor_value']  # 设置只读字段，不允许更改
    ordering = ('incubator_id',)  # 定义列表显示的顺序，负号表示降序


class AdviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'incubator_id', 'time', 'humidity', 'temperature', 'light', 'pres', 'message')
    # fx_fields = ['incubator_incubator_id', 'incubator_incubator_type']
    # list_display_links = ('curTime', 'light', 'pressure')
    list_per_page = 50  # 定义后台列表显示时每页显示数量
    # 定义后台列表显示时能够筛选的字段(会列出所有的可筛选值)
    list_filter = ('incubator_id', 'time')
    search_fields = ('incubator_id', 'time')  # 指定能搜索哪些字段
    #  list_editable = ['name', 'gender']  # 定义可以直接在列表页进行更改的字段
    # fx_fields = ('user_id', )	# 定义列表页显示的外键字段，会直接显示关联的值
    # filter_horizontal = ('posts')	# 显示多对多字段
    readonly_fields = ['id', 'incubator_id', 'time', 'humidity', 'temperature', 'light', 'pres',
                       'message']  # 设置只读字段，不允许更改
    ordering = ('incubator_id',)  # 定义列表显示的顺序，负号表示降序


admin.site.register(models.FixList, FixListAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Incubator, IncubatorAdmin)
admin.site.register(models.Plant, PlantAdmin)
admin.site.register(models.Camera, CameraAdmin)
admin.site.register(models.IncubatorHistory, IncubatorHistoryAdmin)
admin.site.register(models.Device, DeviceAdmin)
admin.site.register(models.Control, ControlAdmin)
admin.site.register(models.Sensor, SensorAdmin)
admin.site.register(models.Advice, AdviceAdmin)

# admin.site.register(models.Administrator)


admin.site.site_header = '中草药管理系统'
admin.site.site_title = '中草药管理系统'
