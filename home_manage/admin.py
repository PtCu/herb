from django.contrib import admin

# Register your models here.
from home_manage import models


class LinkAdmin(admin.ModelAdmin):
    list_display = ("create_time", "link_title", "policy_link", "link_type")
    list_per_page = 15
    ordering = ("-create_time",)
    list_filter = ("create_time", "link_title", "link_type")
    date_hierarchy = 'create_time'


admin.site.register(models.Link, LinkAdmin)


class HomeImageAdmin(admin.ModelAdmin):
    list_display = ("id", "create_time", "image")
    list_per_page = 15
    ordering = ("-create_time",)
    list_filter = ("create_time",)
    date_hierarchy = 'create_time'


admin.site.register(models.HomeImage, HomeImageAdmin)


class IncubatorInfoAdmin(admin.ModelAdmin):
    list_display = ("create_time", "image", "title", "description")
    list_per_page = 15
    ordering = ("-create_time",)
    list_filter = ("create_time", "title")
    date_hierarchy = 'create_time'


admin.site.register(models.IncubatorInfo, IncubatorInfoAdmin)


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ("time", "type_title", "type_desc")
    list_per_page = 15
    ordering = ("-time",)
    list_filter = ("time", "type_title")
    date_hierarchy = 'time'


admin.site.register(models.Advantage, AdvantageAdmin)
