from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from models import *

def index(request):
      
    context = { }
    return render_to_response ('index.html', context, context_instance = RequestContext(request))
