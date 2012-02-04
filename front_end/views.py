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
from models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.core.mail import EmailMessage

#Functions 
def sendusermail(email):
	body = '''
			Hi, 

			Thank you for subscribing with MuviDB. Your login link is http://www.muvidb.com

			Thanks,
			MuviDB team
			'''
	email = EmailMessage('Thank you for subscribing to MuviDB', body, 'noreply@muvidb.com',[email])
	email.send(fail_silently=True)
	return True
	

def register_view(request,template='popup/register.html'):
	form = RegistrationForm()
	context={'form':form }
	return render_to_response(template, context, context_instance = RequestContext(request)) 
	
@csrf_exempt
def register(request,to_return=''):
	if request.method == 'POST':
			form = RegistrationForm(data=request.POST, files=request.FILES)
			if form.is_valid():            
					new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
					new_user.save()
					user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
					profile = UserProfile.objects.create(user=new_user) 
					profile.send_me_daily_email=False
					profile.save()
					#sendusermail(form.cleaned_data['email'])
					login(request, user)
					to_return={'success':True ,'url':reverse('edit_profile_page')}
					#return HttpResponseRedirect(reverse('edit_profile_page'))
			else:
				to_return={'success':False,'message':''}
	return HttpResponse(simplejson.dumps(to_return), mimetype='application/json')
	
def myaccount(request):
	if not request.user.is_anonymous():
		user=request.user
		profile=user.get_profile()
	else:
		return HttpResponseRedirect(reverse('index'))
		
	context={'profile':profile}
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

	context = { 'days' : range(1, 32), 'months' : MONTHS, 'years' : range(1900, 2012), 'current_password' : current_password, 'new_password' : new_password,
			   'confirm_password' : confirm_password, 'password_error' : password_error, }
	
	return render_to_response('main/edit_profile_page.html', context, context_instance = RequestContext(request))
