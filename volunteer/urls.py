from django.conf.urls.defaults import *

urlpatterns = patterns('volunteer.views',

	(r'^thanks/$', 'thanks', ),
	(r'^$', 'volunteer', ),

)