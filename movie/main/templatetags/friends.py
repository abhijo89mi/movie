from django import template
from django.conf import settings
from movie.main.models import Movie,Countries
from front_end.models import *

register = template.Library()

@register.filter
def sent_friend_request(obj, user):
    if Friend.objects.filter(user_requesting=obj, user_accepting=user, are_friends=False):
        return True
    return False

@register.filter
def are_friends(obj, user):
    if Friend.objects.filter(user_requesting=obj, user_accepting=user, are_friends=True):
        #Add to user profile friend manyto many field
        obj.get_profile().friends.add(user)
        user.get_profile().friends.add(obj)
        return True
    return False

@register.filter
def display_name(obj):
    if not obj:
        return 'Anonymous'
    if obj.first_name:
        return obj.first_name+' '+ str(obj.last_name)[0].upper() + '.'
    return obj.username

@register.filter
def friend_requests(obj):
    return Friend.objects.filter(user_accepting=obj, are_friends=False)
 
   
