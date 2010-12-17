from django.conf.urls.defaults import *
from greenparty.news.models import Event




info_dict = {
	'queryset': Event.objects.filter(draft=False),
	'date_field': 'date',
}


urlpatterns = patterns('greenparty.news.views',

	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/(?P<slug>[\w-]+)/$', 'event_detail'),

	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$','event_day',),

	(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'event_month', ),

	(r'^(?P<year>\d{4})/$', 'event_year',),

	(r'^$','event_index', ),

)





