#coding=utf-8
from django.conf.urls import patterns, include, url
from logs import views

urlpatterns = [
    url(r'$', views.logs,name='logs'),
]