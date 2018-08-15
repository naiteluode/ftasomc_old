from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin


import models

from django.shortcuts import render_to_response,render,HttpResponse

from django.contrib.admin.views.decorators import staff_member_required

from django.conf.urls import patterns, include, url
# Register your models here.

class HostListAdmin(admin.ModelAdmin):
    search_fields = ('hostname','ip')
    list_display = ('ip','hostname','application','product','system','status','remark')
    
admin.site.register(models.HostList,HostListAdmin)