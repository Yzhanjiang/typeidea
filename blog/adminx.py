# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from  .models import Post,Category,Tag
import xadmin
from xadmin.layout import Fieldset, Row
from  typeidea.adminx import BaseOwnerAdmin

class PostAdmin(object):
    style_fields = {"content": "ueditor"}
    list_display = ['title','desc','content','status_show','owner','created_time','pv','uv']
    list_display_links = []
    list_filter = ['category','title']
    # fields = ('name',)
    search_fields = ['title','category_name','owner_username']
    save_on_top = True
    show_full_result_count = True

    # actions_on_bottom = True
    # date_hierarchy = 'created_time'
    # list_editable = ('title',)
    exclude = ['html','pv','uv']

    # fields = (
    #     ('category','title'),
    #     'desc',
    #     'status',
    #     ('content', 'is_markdown'),
    #     'html',
    #     'tag',
    #     'owner',
    # )
    form_layout = (
        Fieldset(
            '基础信息',
            'title',
            'desc',
            Row('category', 'status', 'is_markdown'),
            'content',
            'tag',
            'owner',
        ),
    )



class CategoryAdmin(object):
    list_display = ['name','status','is_nav','owner','created_time']

class TagAdmin(object):
    list_display = ['name', 'status', 'owner', 'created_time']

xadmin.site.register(Post,PostAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)

