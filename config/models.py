# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
class Link(models.Model):
    STATUS_ITEMS = (
        (1,'正常'),
        (1,'删除'),
    )
    title = models.CharField(max_length=50,verbose_name="标题")
    href = models.URLField(verbose_name="连接")
    status = models.PositiveIntegerField(default=1,choices=STATUS_ITEMS,verbose_name="状态")
    weight = models.PositiveIntegerField(default=1,choices=zip(range(1,6),range(1,6)),
                                         verbose_name="权重",
                                         help_text="权重越高展示顺序越靠前")

    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '友链'


class SideBar(models.Model):
    STATUS_ITEMS = (
        (1, '展示'),
        (2, '下线'),
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最近评论'),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE,
                                               verbose_name="展示类型")

    content = UEditorField('内容', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')
    # content = models.CharField(max_length=500, blank=True, verbose_name="内容",
    #                            help_text="如果设置的不是HTML类型，可为空")
    status = models.PositiveIntegerField(default=1,choices=STATUS_ITEMS,verbose_name="状态")

    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"