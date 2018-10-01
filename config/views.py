# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.

from  django.views.generic import ListView
from blog.views import CommonMixin
from  django.conf import  settings

from comment.models import Comment
from comment.views import CommentShowMixin
from  .models import Link
from comment.forms import CommentForm

class LinkView(CommonMixin,CommentShowMixin,ListView):
    # model = Link
    queryset = Link.objects.filter(status=1)
    template_name = settings.THEME + '/config/links.html'
    context_object_name = 'links'
    # allow_empty = True









