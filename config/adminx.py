# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import xadmin
# Register your models here.

from .models import Link,SideBar

class LinkAdmin(object):
    pass

class SideBarAdmin(object):
    pass

xadmin.site.register(Link,LinkAdmin)
xadmin.site.register(SideBar,SideBarAdmin)