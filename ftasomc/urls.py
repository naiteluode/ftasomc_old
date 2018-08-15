#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from ops import api_urls,cus_admin,views
from ansibleweb import ansible_urls,views
from asset import asset_urls,views
from cobblerweb import cobbler_urls,views
from logs import logs_urls,views
from monitor import monitor_urls,views
#from ansiblewebapp import ansiblewebapp_urls,views

if settings.DEBUG:
    import debug_toolbar
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'python_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'session_security/', include('session_security.urls')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^doc/$', 'ops.views.doc'),
    url(r'^$', 'ops.views.dashboard'),
    url(r'^login/$', 'ops.views.login',name='login'),
    url(r'^assets/$', 'ops.views.assets'),
    url(r'^assetsloc/$', 'ops.views.assets_loc'),
    url(r'^install/$', 'ops.views.install'),
#    url(r'^assets_add/$', 'ops.views.assets_add'),
#    url(r'^exportassets/$', 'ops.views.exportassets'),
    url(r'^user/$', 'ops.views.user'),
    url(r'^change/$', 'ops.views.change'),
    url(r'^personal/','ops.views.personal',name='personal'),
#    url(r'^filechange/$', 'ops.views.filechange'),
#    url(r'^salt/$', 'ops.views.saltstack'),
#    url(r'^saltcmd/$','ops.views.saltcmd'),
#    url(r'^remote_execution/$','ops.views.remote_execution'),
#    url(r'^saltminion/$','ops.views.saltminion'),
#    url(r'^saltstatus/$','ops.views.saltstatus'),
#    url(r'^saltdeploy/$','ops.views.saltdeploy'),
#    url(r'^saltupload/$','ops.views.saltupload'),
#    url(r'^saltfile/$','ops.views.saltfile'),
#    url(r'^saltgroup/$','ops.views.saltgroup'),
#    url(r'^saltsysuser/$','ops.views.saltsysuser'),
#    url(r'^saltlog/$','ops.views.saltlog'),
    url(r'^file/$', 'ops.views.file'),
    url(r'^monitor/$','ops.views.monitor'),
    url(r'^test/$','ops.views.test'),
    url(r'^test1/$','ops.views.test1'),
#    url(r'^hostinfo/$','ops.views.hostinfo'),
#    

    ####用户管理####
    url(r'^personal/','ops.views.personal',name='personal'),
    url(r'^user_audit/(\d+)/$','ops.views.user_audit', name='user_audit'),
    url(r'^logout/$','ops.views.logout',name='logout'),
    url(r'^user_del/$', 'ops.views.user_del', name='user_del'),
    #url(r'^user_edit/$', 'ops.views.user_edit', name='user_edit'),
    
    ####主机管理####
    url(r'^hosts/$', 'ops.views.hosts',name='host_list'),
    url(r'^hosts/multi/$', 'ops.views.hosts_multi'),
    url(r'^hosts/multi/filetrans$','ops.views.hosts_multi_filetrans'),
    url(r'^hosts/crontab/$','ops.views.crontab'),
    url(r'^multi_task/log/deatail/(\d+)/$','ops.views.multi_task_log_detail',name='multi_task_log_detail'),
    url(r'^host/detail/', 'ops.views.host_detail'),
    url(r'multitask/cmd/$', 'ops.views.multitask_cmd',name='multitask_cmd'),
    url(r'multitask/res/$', 'ops.views.multitask_res'),
    url(r'multitask/file_download/(\d+)/$', 'ops.views.file_download', name='file_download_url'),
    url(r'multitask/file_upload/$', 'ops.views.multitask_file_upload'),
    url(r'multitask/file/$', 'ops.views.multitask_file',name='multitask_file'),
    url(r'multitask/action/$', 'ops.views.multitask_task_action',name='multitask_action'),
    url(r'token/gen/$', 'ops.views.token_gen',name='token_gen'),
    url(r'dashboard_summary/$', 'ops.views.dashboard_summary',name='dashboard_summary'),
    url(r'dashboard_detail/$', 'ops.views.dashboard_detail',name='dashboard_detail'),
    url(r'audit/user_counts/$', 'ops.views.user_login_counts',name='user_login_counts'),
    url(r'audit/cmd_logs/$', 'ops.views.audit_cmd_logs'),
    
    ####Ansible管理####
    url(r'^ansible/',include(ansible_urls)),
    
     ####AnsibleWebApp管理####
#    url(r'^ansiblewebapp/',include(ansiblewebapp_urls)),
    
    ####Asset管理####
    url(r'^asset/',include(asset_urls)),
    
    ####Cobbler管理####
    url(r'^cobbler/',include(cobbler_urls)),
    
    ####Log管理####
    url(r'^logs/',include(logs_urls)),
    
    ####Monitor管理####
    url(r'^monitor/',include(monitor_urls)),
)
