from front_end.models import *

def menu(request):
    navigations = Navigation.objects.filter(publish=True)
    members = Team_Members.objects.filter(publish=True)
    return {'navigations' : navigations,'members':members }
