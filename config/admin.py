# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Link,SideBar

class LinkAdmin(admin.ModelAdmin):
    pass

class SideBarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Link,LinkAdmin)
admin.site.register(SideBar,SideBarAdmin)