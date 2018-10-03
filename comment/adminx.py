# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import xadmin
# Register your models here.

from  .models import Comment,CommentTest

class CommentAdmin(object):
    style_fields = {"content": "ueditor"}
    list_display = ['target','nickname','content','website','created_time']

xadmin.site.register(Comment,CommentAdmin)

class CommentTestAdmin(object):
    style_fields = {"content":"ueditor"}
    list_display = ['Name','content']

xadmin.site.register(CommentTest,CommentTestAdmin)