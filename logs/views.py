# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from ftasomc import settings

# Create your views here.
def logs(request):
	return render_to_response('logs.html')
