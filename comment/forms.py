#!/usr/bin/env python 
#coding:utf8

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) <10:
            raise forms.ValidationError('长度太短！！')

    class Meta:
        model = Comment
        fields = ['nickname','email','website','content']

