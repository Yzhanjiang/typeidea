# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

from  django.views.generic import ListView
from blog.views import CommonMixin
from  django.conf import  settings
from  .models import Link

class LinkView(CommonMixin,ListView):
    model = Link
    template_name = settings.THEME + '/config/links.html'
    context_object_name = 'links'
    allow_empty = True
    queryset = Link.objects.filter(status=1)







