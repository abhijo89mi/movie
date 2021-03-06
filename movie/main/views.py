from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from models import *
from form import *
from datetime import datetime
from front_end.models import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from recaptcha_works.decorators import fix_recaptcha_remote_ip

@fix_recaptcha_remote_ip
def index(request,template=''):
  error=''
  if request.user.is_anonymous():
      if request.POST:
        form = LoginForm(data=request.POST)
        if form.is_valid():
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password) 
          if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
          else :
            error="Sorry ... User name or password error , Try again !"
        else:
          error="User name or password missing  !"
      else:
        form=LoginForm()
  else:
    return HttpResponseRedirect(reverse('home'))
    
  context={'login_form':form,'error':error}
  return render_to_response('main/startup.html', context, context_instance = RequestContext(request))
  
def home(request,template='main/index.html'):
  if request.user.is_anonymous():
	return HttpResponseRedirect(reverse('index'))
  today = datetime.date.today()
  boxoffice_movies =Boxoffice.objects.order_by('-imdbid__rating')[:2]
  intheater_movies =Intheaters.objects.order_by('-imdbid__rating')[:2]
  
  
  context={
    
    'boxoffice_movies':boxoffice_movies,
    'intheater_movies':intheater_movies
  
  }
  return render_to_response('main/index.html', context, context_instance = RequestContext(request))

def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse('index'))

def movie_info(request , movie_id):
  if request.user.is_anonymous():
	return HttpResponseRedirect(reverse('index'))
  movie=Movie.objects.get(id=movie_id)
  context={'movie':movie}
  return render_to_response('main/movie_info.html', context, context_instance = RequestContext(request))
