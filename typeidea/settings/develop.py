#!/usr/bin/env python 
#coding:utf8

from  .base import  *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '192.168.88.135',
        'PORT': '3306',
    }
}