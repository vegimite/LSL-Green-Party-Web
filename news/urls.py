from django.conf.urls.defaults import *
from news.models import Event


urlpatterns = patterns('news.views',

	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/(?P<slug>[\w-]+)/$', 'event_detail'),

	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$','event_day',),

	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'event_month', ),

	(r'^(?P<year>\d{4})/$', 'event_year',),

	(r'^$','event_index', ),

)





