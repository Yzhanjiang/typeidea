# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import xadmin
# Register your models here.

from  .models import Comment

class CommentAdmin(object):
    list_display = ['target','nickname','content','website','created_time']

xadmin.site.register(Comment,CommentAdmin)