#!/usr/bin/env python 
#coding:utf8

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    # target = forms.CharField(max_length=100, widget=forms.widgets.HiddenInput)
    nickname = forms.CharField(
        max_length=50,
        label='昵称',
        widget=forms.widgets.Input(
            attrs={'class':'form-control','style':"width:60%;"}
        )
    )
    email = forms.CharField(
        max_length=50,
        label='Email',
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control','style':"width:60%;"}
        )
    )
    website = forms.CharField(
        max_length=100,
        label='网站',
        widget=forms.widgets.URLInput(
            attrs={'class': 'form-control','style':"width:60%;"}
        )
    )

    content = forms.CharField(
        label="内容",
        max_length=500,
        widget=forms.widgets.Textarea(attrs=({'rows':6,'cols':60,'class':'form-control','style':"width:60%;"}))
    )

    def clean_content(self):
        content = self.cleaned_data.get('content')
        print("content:{0}".format(content))
        if len(content) <10:
            raise forms.ValidationError('长度太短！！')
        return content

    class Meta:
        model = Comment
        fields = ['nickname','email','website','content']

