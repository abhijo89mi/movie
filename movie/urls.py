from django.conf.urls.defaults import *
from autoregister import autoregister
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
autoregister('main')
autoregister('front_end')
urlpatterns = patterns('movie.main',
    # Examples:
    url(r'^$', 'views.index', name='home'),
    # url(r'^movie/', include('movie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # ============ URL FOR USER TRACKING=====================
    (r'^tracking/', include('tracking.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )


if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'static/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
