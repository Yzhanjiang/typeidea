# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from  .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['target','nickname','content','website','created_time']

admin.site.register(Comment,CommentAdmin)