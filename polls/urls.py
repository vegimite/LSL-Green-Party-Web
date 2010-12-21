from django.conf.urls.defaults import *

urlpatterns = patterns('polls.views',

	(r'^(?P<slug>[\w-]+)/vote/$', 'poll_vote'),
	(r'^(?P<slug>[\w-]+)/$', 'poll_detail'),
	(r'^$','poll_index', ),
)