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
    url(r'^logout/$', 'views.logout_view', name='logout'),
    url(r'^movie/(?P<movie_id>.*)/$','views.movie_info',name='movie'),
    
    
    # ============ URL FOR USER TRACKING=====================
    (r'^tracking/', include('tracking.urls')),
    
    # =========== ADMIN URL ================================
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
)

urlpatterns += patterns('front_end',
      #TEmplate view
      url(r'^new_account$','views.register_view',name='register_view'),
      #From submit
      url(r'^register$','views.register',name='register'),
      url(r'^home/myaccount/$','views.myaccount',name='myaccount'),
      url(r'^home/profile/(?P<user_id>.*)/$', 'views.myaccount', name='user_page'),
      url(r'user/request/(?P<user_id>.*)/$', 'views.friend_request', name='friend_request'),
      url(r'user/accept/(?P<user_id>.*)/$', 'views.friend_accept', name='friend_accept'),
      url(r'^home/myaccount/edit_profile_page/$','views.edit_profile_page',name='edit_profile_page'),
      url(r'home/myaccount/edit_profile_page/delete-pic/$', 'views.delete_pic', name='delete_pic'),
      url(r'home/myaccount/edit_profile_page/profile-pic/$', 'views.profile_pic', name='profile_pic'),
      

)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
    
urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve'),
)
    
    

