#coding=utf-8
from django.conf.urls import patterns, include, url
from asset import views

urlpatterns = [
    #url(r'^host/list/$', views.host_list,name='host_list'),
    url(r'^host/manage/$', views.host_list_manage,name='host_manage'),
    url(r'^add_host/$', views.host_list_manage, name='add_host'),
    url(r'^delete_host/$', views.host_list_manage, name='host_delete'),
]