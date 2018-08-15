#coding=utf-8
from django.conf.urls import patterns, include, url
from monitor import views
from monitor.views import GetGrapidAPIView

urlpatterns = [
    url(r'hosts/$', views.host,name='monitor_hosts'),
    url(r'applications/$', views.application,name='monitor_applications'),
    url(r'services/$', views.service,name='monitor_services'),
    url(r'api/getgraphid/(\d+)/$', GetGrapidAPIView.as_view(),),
]