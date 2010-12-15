# Create your views here.
from django.shortcuts import render_to_response
from django.utils import translation
from greenparty.news.models import  Event

def setLang(list, language):
    for l in list:
        l.lang = language
    return list



def events(request, language):
    events = setLang(Event.objects.filter(draft=False), language)
    translation.activate(language)
    return render_to_response('events/events.html', ({'events' : events, 'language' : language,}))
