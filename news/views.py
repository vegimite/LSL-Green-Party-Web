# Create your views here.
from django.shortcuts import render_to_response
from greenparty.news.models import Bio, Event

def setLang(list, language):
    for l in list:
        l.lang = language
    return list

def bios_default(request, language):
    b = setLang(Bio.objects.all(), language)
    default = Bio.objects.all()[0]
    default.lang = language
    return render_to_response('bio/bios.html', ({'bios' : b, 'bio' : default, 'language' : language,}))


def bios(request, language, bio_id):
    b = setLang(Bio.objects.all(), language)
    bio = Bio.objects.get(id=bio_id)
    bio.lang = language
    return render_to_response('bio/bios.html', ({'bios' : b, 'bio' : bio, 'language' : language,}))


def events(request, language):
    events = setLang(Event.objects.all(), language)
    return render_to_response('events/events.html', ({'events' : events, 'language' : language,}))
