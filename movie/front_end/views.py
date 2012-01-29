from django.contrib.auth.models import check_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson
from movie.main.form import *
from django.contrib.auth import authenticate, login, logout

def register_view(request,template='popup/register.html'):
	if request.method == 'POST':
			form = RegistrationForm(data=request.POST, files=request.FILES)
			if form.is_valid():            
					new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
					user = authenticate(username=new_user.username, password=form.password)
					login(request, user)
					return HttpResponseRedirect(reverse('index'))
	else:
			form = RegistrationForm()
	context={'form':form}
	return render_to_response(template, context, context_instance = RequestContext(request)) 
	
def register(request,to_return=''):
	if request.method == 'POST':
			form = RegistrationForm(data=request.POST, files=request.FILES)
			if form.is_valid():            
					new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
					user = authenticate(username=new_user.username, password=new_user.password)
					login(request, user)
					
			else:
				to_return={'message':form.errors,}
	return HttpResponse(simplejson.dumps(to_return), mimetype='application/json')
	
def myaccount(request):
	context={}
	
	return render_to_response('main/myaccount.html', context, context_instance = RequestContext(request))

