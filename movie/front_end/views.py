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
from movie.helper import *

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
	allow_admin=False
	
	user=request.user
	profile=user.get_profile()
	if user.is_staff :
		allow_admin=True
	if not user.first_name and not user.last_name :
		#User not finish the registration , 
		return HttpResponseRedirect(reverse('edit_profile_page'))
	
	context={}
	return render_to_response('main/myaccount.html', context, context_instance = RequestContext(request))

def edit_profile_page(request):
	current_password = request.POST.get('current_password', '')
	new_password = request.POST.get('new_password', '')
	confirm_password = request.POST.get('confirm_password', '')
	password_error = ''

	if request.POST:
		gender = request.POST.get('gender', '')
		first_name = request.POST.get('first_name', '')
		last_name = request.POST.get('last_name', '')
		email = request.POST.get('email', '')
		day = request.POST.get('day', '')
		month = request.POST.get('month', '')
		year = request.POST.get('year', '')
		user = request.user
		user.first_name = first_name
		user.last_name = last_name
		user.email = email
		user.get_profile().gender = gender
		
		if day.isdigit() and month.isdigit() and year.isdigit():
			date = datetime.date(int(year), int(month), int(day))
			user.get_profile().birthday = date

		if current_password:
			if not new_password or not confirm_password:
				password_error = 'All fields are required'
			if not password_error:
				if check_password(current_password, user.password ):
					if new_password == confirm_password:
						user.set_password(new_password)
						user.get_profile().has_blank_password = False
						password_error = 'Your password has been updated successfully.'
					else:
						password_error = 'The two passwords don\'t match'
				else:
					password_error = 'The current password you entered doesn\'t match our records.'

		user.save()
		user.get_profile().save()

	context = { 'tab' : 'Edit My Profile', 'days' : range(1, 32), 'months' : MONTHS, 'years' : range(1900, 2012), 'current_password' : current_password, 'new_password' : new_password,
			   'confirm_password' : confirm_password, 'password_error' : password_error, }
	return render_to_response('main/edit_profile_page.html', context, context_instance = RequestContext(request))
