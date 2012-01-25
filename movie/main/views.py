from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from models import *

def index(request):
    context = {}
    return render_to_response('main/index.html', context, context_instance = RequestContext(request))
