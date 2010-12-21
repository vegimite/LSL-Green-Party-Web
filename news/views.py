# Create your views here.
from django.shortcuts import render_to_response
from django.utils import translation
from django.views.generic.date_based import archive_index, archive_year, archive_month, archive_day, object_detail
from news.models import  Event


info_dict = {
	'queryset': Event.objects.filter(draft=False),
	'date_field': 'date',
}

def event_index(request, language):
    Event.lang = language
    translation.activate(language)
    return archive_index(request, Event.objects.filter(draft=False), 'date', extra_context={'language':language, 'base_url':''}, template_name='events/event_list.html', template_object_name='object_list')

def event_year(request, language, year):
    Event.lang = language
    translation.activate(language)
    base_url = '/%s' % (year)
    return archive_year(request, year, Event.objects.filter(draft=False), 'date', extra_context={'language':language, 'base_url':base_url}, template_name='events/event_list.html', make_object_list=True)

def event_month(request, language, year, month):
    Event.lang = language
    translation.activate(language)
    base_url = '/%s/%s' % (year, month)
    return archive_month(request, year, month, Event.objects.filter(draft=False), 'date', extra_context={'language':language, 'base_url':base_url}, template_name='events/event_list.html', allow_empty=True)

def event_day(request, language, year, month, day):
    Event.lang = language
    translation.activate(language)
    base_url = '/%s/%s/%s' % (year, month, day)
    return archive_day(request, year, month, day, Event.objects.filter(draft=False), 'date', extra_context={'language':language, 'base_url':base_url}, template_name='events/event_list.html', allow_empty=True)

def event_detail(request, language, year, month, day, slug):
    Event.lang = language
    translation.activate(language)
    base_url = '/%s/%s/%s' % (year, month, day)

    if language == 'fr':
        slug_field = 'slug_french'
    else:
        slug_field = 'slug_english'

    return object_detail(request, year, month, day, Event.objects.filter(draft=False), 'date', slug=slug, slug_field=slug_field, extra_context={'language':language, 'base_url':base_url}, template_name='events/event_detail.html', template_object_name='event')

def events(request, language):
    events = setLang(Event.objects.filter(draft=False), language)
    translation.activate(language)
    return render_to_response('events/events.html', ({'events' : events, 'language' : language,}))
