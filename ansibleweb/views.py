#!/usr/bin/env python
#coding=utf-8
from django.shortcuts import render,render_to_response,redirect,HttpResponseRedirect,HttpResponse
from ftasomc import settings
from django.db import models

from django.contrib import auth

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

####ansible####
import time,os,utils
import multiprocessing, threading
import base64
import csv
import ansible.runner
from ansible.inventory import Inventory
import simplejson
import hashlib
from ftasomc.settings import NUMBER_OF_TASK_PER_PAGE
from ansibleweb.models import Task
from django.contrib.admin.views.decorators import staff_member_required
from ansibleweb.comm import *


def ansible(request):
	return render_to_response('ansible.html')
	
def ansiblecmd(request):
	output = ''
	if request.method == 'POST':
		command = request.POST.get('command')
		output = os.popen(command).read()
	return render_to_response('ansible_cmd.html',{'output':output})
	
def ansiblegroup(request):
    #user = request.user
    #msgnum = Msg.objects.filter(isread=0,msgto=user).count()
    if request.method == 'POST':
        groupname = request.POST['groupname']
        hosts = request.POST['hosts']
        if request.POST.has_key("add"):
            os.popen('sudo echo -e "[%s]\n %s" >> %s' % (groupname,hosts,ansiblegroupsconf))
        if request.POST.has_key("modf"):
            os.popen('sudo sed -i "s/[%s]/%s/" %s' % (groupname,groupname,ansiblegroupsconf))
            os.popen('sudo sed -i "s/%s/%s/" %s' % (hosts,hosts,ansiblegroupsconf))
        if request.POST.has_key("del"):
            os.popen('sudo sed -i "/[%s]/d" %s' % (groupname,ansiblegroupsconf))
    a = file(ansiblegroupsconf).readlines()
    #fp = open(ansiblegroupsconf,'r')
    #a = fp.readlines()
    #fp.close()
    a.remove('\n')
    rets = {}
    for i in a:
       if str(i).find('[') == 0:
        groupname = i.strip()
       else:
        hosts = i.rstrip('\n')
        rets[groupname] = hosts
    return render_to_response('ansible_group.html',locals())

@staff_member_required    
def ansiblebatch(request):
    if request.method == 'POST':
        inventory = request.POST.get('inventory', '')
        cmd = request.POST.get('cmd', '')
        if '' in [inventory.strip(), cmd.strip()]:
            return redirect('/ansible/batch')
        run_task(request, inventory, cmd)
        return redirect('/ansible/batch')
    else:
        tasks = Task.objects.all().order_by('-id')[:NUMBER_OF_TASK_PER_PAGE]
	return render_to_response('ansible_batch.html', locals())

@staff_member_required	
def ansibledetail(request, id):
    assert(request.method == 'GET')
    jobid = request.GET.get('jobid', '')
    if jobid.isdigit():
        jobid = int(jobid)
    else:
        jobid = -1
    task = Task.objects.get(id = id)
    #jobs = task.job_set.all().order_by('-rc')
    jobs = task.job_set.all()
    jobs_succeed = [ job for job in jobs if job.rc == 0 ]
    jobs_failed = [ job for job in jobs if job.rc != 0 ]
    jobs = jobs_failed + jobs_succeed
    return render_to_response('ansible_detail.html', locals())

def run_task(request, inventory, cmd):
    task = Task()
    task.inventory = inventory
    task.cmd = cmd
    task.farmer = request.user.username
    task.run()
    
@staff_member_required
def ansibleretry(request, id):
    assert(request.method == 'GET')
    task = Task.objects.get(id = id)
    failure_hosts = [job.host for job in task.job_set.all() if job.rc != 0]
    assert(failure_hosts)
    inventory = ':'.join(failure_hosts)
    run_task(request, inventory, task.cmd)
    return redirect('/ansible/batch')
    
@staff_member_required
def ansiblererun(request, id):
    assert(request.method == 'GET')
    task = Task.objects.get(id = id)
    run_task(request, task.inventory, task.cmd)
    return redirect('/ansible/batch')
    
def ansiblelog(request):
	output = ''
#	f = open(ansiblelog)
#	try:
#	    output = f.read()
#	finally:
#	    f.close()
#
	return render_to_response('ansible_log.html',{'output':output})
	
def ansibleinspection(request):
	output = ''
	if request.method == 'POST':
		command = request.POST.get('command')
		output = os.popen(command).read()
	return render_to_response('ansible_inspection.html',{'output':output})