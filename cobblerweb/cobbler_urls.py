#coding=utf-8
from django.conf.urls import patterns, include, url
from cobblerweb import views

urlpatterns = [
    url(r'^install_list/$', views.system_install_list, name='install_list'),
    url(r'^install_manage/(?P<id>\d+)/$', views.system_install_managed, name='install_manage'),
    url(r'^install_record/$',views.system_install_record, name='install_record'),
    url(r'^system_install/$',views.system_install, name='system_install'),
]