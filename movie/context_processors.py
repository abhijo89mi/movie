from movie.front_end.models import *

def menu(request):
    navigations = Navigation.objects.filter(publish=True)
    return {'navigations' : navigations }
