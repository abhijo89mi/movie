from django import template
from django.conf import settings

register = template.Library()

@register.filter
def roundFloat(obj):
    return obj.split('.')[0].replace(',', '').replace('C$', '$')
    
@register.filter
def add_percentage(obj, percent):
    return int(obj)+(int(obj)*percent/100.00)

@register.filter
def get_first_location(obj):
    for l in obj:
        if l.streetAddress1:
            sa = l.streetAddress1
            code = l.postalCode.code
            if code: code = ', '+code
            city = l.city.name
            return sa+'<br/>'+city+code+'<br/><br/>'

@register.filter
def get_first_location_name(obj):
    for l in obj:
        if l.name:
           return l.name
    return 'You'

@register.filter
def daysleft(obj):
    from datetime import datetime
    diff = obj - datetime.now()
    if diff.days < 0:
        return 'Deal closed...' 
    elif diff.days == 0:
        return 'Last day today to buy.' 
    elif diff.days == 1:
        return str(diff.days) + ' day Left to buy' 
    return str(diff.days) + ' days Left to buy'
    
@register.filter
def user_review_count(obj, page_user):
    business = obj
    count = 0
    for br in business.businessreview_set.all():
        if br.user == page_user:
            count = count + 1    
    return count

@register.filter
def ordered_by_pins(obj):
    return sorted(list(obj.object_list), key=lambda b: b.userprofile_set.count(), reverse=True)
    
@register.filter
def filter_by_id(obj):
    return obj.order_by('id')

@register.filter
def randomize(obj):
    return obj.order_by('?')

@register.filter
def order_alphabetically(obj):
    return obj.order_by('name')
    
@register.filter
def filter_in_city(obj, city):
    return obj.filter(address__city__name=city.name)
    