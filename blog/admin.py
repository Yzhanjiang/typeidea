# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from  .models import Post,Category,Tag


class PostAdmin(admin.ModelAdmin):
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
    # exclude = ['owner']

    fields = (
        ('category','title'),
        'desc',
        'status',
        ('content', 'is_markdown'),
        'html',
        'tag',
        'owner',
    )



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','status','is_nav','owner','created_time']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'owner', 'created_time']

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)

