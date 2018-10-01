# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from  django.views.generic import  TemplateView
from  django.conf import  settings
# Create your views here.

from  .forms import CommentForm
from  .models import Comment

class CommentShowMixin(object):
    def get_comments(self):
        target = self.request.path
        print("target:{0}".format(target))
        comments = Comment.objects.filter(target=target)
        return comments

    def get_context_data(self,**kwargs):
        kwargs.update({
            'comment_form':CommentForm(),
            'comment_list':self.get_comments(),
        })
        print("kwargskwargskwargskwargskwargs")
        print(kwargs)
        return  super(CommentShowMixin,self).get_context_data(**kwargs)






class CommentView(TemplateView):
    template_name = settings.THEME + '/comment/result.html'

    def get(self, request, *args, **kwargs):
        return  super(CommentView,self).get(request, *args, **kwargs)

    def post(self ,request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        target = request.POST.get('target')

        # print(request.POST)
        # print(comment_form)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.target = target
            instance.save()
            succeed = True
            return  redirect(target)
        else:
            succeed = False
        context = {
            'succeed':succeed,
            'form':comment_form,
            'target':target,
        }
        return self.render_to_response(context)







