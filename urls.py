from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^greenparty/', include('greenparty.foo.urls')),
    (r'^$',                                                 'home.views.redirect'),
    (r'^(?P<language>(en|fr))/$',                           'home.views.home'),
    (r'^(?P<language>(en|fr))/calendar/$',                  'home.views.calendar'),
    (r'^(?P<language>(en|fr))/donate/$',                    'home.views.donate'),
    (r'^(?P<language>(en|fr))/join/$',                      'home.views.join'),


    (r'^(?P<language>(en|fr))/volunteer/',                  include('volunteer.urls')),
    (r'^(?P<language>(en|fr))/media/',                      include('news.urls')),
    (r'^(?P<language>(en|fr))/polls/',                      include('polls.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),


    #media path
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': './media/'}),
)
