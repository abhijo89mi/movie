from django import template
from django.conf import settings
from movie.main.models import *
from front_end.models import *

register = template.Library()

@register.filter
def get_cast_charactor_name(obj):
	return obj.all()[0]
	
@register.filter
def get_cast_photo(obj):
	try :
		photo_url =obj.photo.all()[0]
		if not photo_url:
			photo_url='no_photo.jpg'
		else:
			photo_url=photo_url
	except :
		photo_url='no_photo.jpg'
	return photo_url
	
