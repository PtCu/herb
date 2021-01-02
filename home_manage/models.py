from django.db import models


# Create your models here.
class Link(models.Model):
    create_time = models.DateTimeField("时间", auto_now=True)
    link_title = models.CharField("链接标题", max_length=50,blank=True)
    policy_link = models.CharField("相关链接", max_length=200)
    link_type = models.CharField("链接类型", choices=(('国家政策', '国家政策'), ('中草药培养指南', '中草药培养指南'),
                                                  ('培养箱使用手册', '培养箱使用手册'), ('草药市场行情', '草药市场行情')),
                                 default='相关政策', max_length=50)

    class Meta:
        managed = True
        verbose_name = '相关链接'
        verbose_name_plural = '相关链接'

    def __str__(self):
        return '相关链接' + str(self.id)


class HomeImage(models.Model):
    create_time = models.DateTimeField("创建时间", auto_now=True)
    image = models.ImageField("轮播图", upload_to='static/home_images')

    class Meta:
        managed = True
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'

    def __str__(self):
        return '轮播图' + str(self.id)


class IncubatorInfo(models.Model):
    create_time = models.DateTimeField("创建时间", auto_now=True)
    image = models.ImageField("图片", upload_to='static/incu_images')
    title = models.CharField('标题', max_length=20)
    description = models.CharField('详细描述', max_length=200)

    class Meta:
        managed = True
        verbose_name = '培养箱介绍'
        verbose_name_plural = '培养箱介绍'

    def __str__(self):
        return '培养箱介绍' + str(self.id)


class Advantage(models.Model):
    time = models.DateTimeField('创建时间', auto_now=True)
    type_title = models.CharField('优势标题', max_length=20)
    type_desc = models.CharField('优势详情', max_length=200)

    class Meta:
        managed = True
        verbose_name = '产品优势'
        verbose_name_plural = '产品优势'

    def __str__(self):
        return '产品优势' + str(self.id)
