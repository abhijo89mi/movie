from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('muvidb.main',

    url(r'^$', 'views.index', name='index'),


)
