from django.conf.urls.defaults import *
from autoregister import autoregister
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
autoregister('main')
autoregister('front_end')
urlpatterns = patterns('movie.main',
    # ============= MAIN URL ===============================
    url(r'^$', 'views.index', name='index'),
    url(r'^home/$', 'views.home', name='home'),
    
    # ============ URL FOR USER TRACKING=====================
    (r'^tracking/', include('tracking.urls')),
    
    # =========== ADMIN URL ================================
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
)

urlpatterns += patterns('movie.front_end',
      #TEmplate view
      url(r'^new_account$','views.register_view',name='register_view'),
      #From submit
      url(r'^register$','views.register',name='register'),
      

)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

