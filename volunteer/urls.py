from django.conf.urls.defaults import *

urlpatterns = patterns('greenparty.volunteer.views',

	(r'^thanks/$', 'thanks', ),
	(r'^$', 'volunteer', ),

)