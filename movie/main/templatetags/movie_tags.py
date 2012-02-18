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
	photo_url =obj.photo.all()
	if not photo_url:
		photo_url='no_photo.jpg'
	else:
		photo_url=photo_url[0]
	return photo_url
	
