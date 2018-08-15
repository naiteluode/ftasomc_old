#coding=utf-8
from django.conf.urls import patterns, include, url
from ansiblewebapp import views

urlpatterns = [
    #url(r'$', views.ansible,name='ansible'),
    url(r'^cmd/$', views.ansiblecmd,name='ansiblecmd'),
    url(r'^batch/$',views.ansiblebatch, name='ansiblebatch'),
    url(r'^detail/(?P<id>\d+)/$',views.ansibledetail, name='ansibledetail'),
    url(r'^retry/(?P<id>\d+)/$', views.ansibleretry, name='ansibleretry'),
    url(r'^rerun/(?P<id>\d+)/$', views.ansiblererun, name='ansiblererun'),
    url(r'^group/$',views.ansiblegroup,name='ansiblegroup'),
    url(r'^log/$', views.ansiblelog,name='ansiblelog'),
    url(r'^inspection/$', views.ansibleinspection,name='ansibleinspection'),
    #url(r'^key/$', views.ansiblekey,name='ansiblekey'),
    #url(r'^playbook/$', views.ansibleplaybook,name='ansibleplaybook'),
]