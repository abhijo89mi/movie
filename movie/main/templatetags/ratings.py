from django import template
from django.conf import settings
from main.models import *

register = template.Library()

@register.filter
def rating(ratings):
    if ratings.count() == 0:
        return 0
    else:
        return ratings.all()[0].rating

@register.filter
def has_rating(obj, business):
    try:
        if obj.filter(business=business):
            return obj.filter(business=business)[0]
    except:
        pass
    return False

@register.filter
def get_rating(obj, business):
    return obj.filter(business=business)[0].rating
    
@register.filter
def rating_title(obj):
    from main.helpers import loadRatingRangeTitles
    rating_string = loadRatingRangeTitles()
    return rating_string[int(obj)]