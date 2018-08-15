# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.views.generic import View
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from ftasomc import settings
from ops.models import Hosts
import json

# Create your views here.
def host(request):
    Host_lists = Hosts.objects.all()
    return render_to_response('host.html',{'Host_lists':Host_lists})
	
def application(request):
	return render_to_response('applications.html')
	
def service(request):
	return render_to_response('services.html')
	
class GetGrapidAPIView(View):
     
    def get(self, request, hostid):
        try:
            hostinfo = Hosts.objects.using('res').get(id=hostid)
            if hostinfo.platid == 34:
                hostip = hostinfo.ip2
            else:
                hostip = hostinfo.ip1
            print "hostip: %s" % hostip
             
            ret = []
            for key in ['system.cpu.util[,idle]', 'net.if.in[eth0]|net.if.in[em1]', 'vm.memory.size[available]', 'icmpping']:
                if '|' in key:
                    key1, key2 = key.split('|')
                    #获取itemid：
                    itemid = Items.objects.using('zab').get(Q(key_field=key1)|Q(key_field=key2), hostid__host=hostip).itemid         
                else:
                    #获取itemid：
                    itemid = Items.objects.using('zab').get(key_field=key, hostid__host=hostip).itemid 
                print "itemid: %s" % itemid
                graphitems = GraphsItems.objects.using('zab').filter(itemid=itemid)[0]
                graphid = graphitems.graphid.graphid
                print "graphid: %s" % graphid
                ret.append(graphid)
        except Exception,e:
            print e
            ret = []
        return HttpResponse(json.dumps(ret))