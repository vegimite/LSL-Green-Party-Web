# Create your views here.
from django.shortcuts import render_to_response
from django.utils import translation
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from home.models import Welcome, Candidate, Aside
from news.models import Event
from polls.models import Poll

def redirect(request):
    if request.LANGUAGE_CODE[0:2] == 'fr':
        return HttpResponseRedirect("/fr/")

    return HttpResponseRedirect("/en/")

def home(request, language):
    Welcome.lang = language
    welcome = Welcome.objects.all()[0]

    Candidate.lang = language
    candidate = Candidate.objects.all()[0]

    Aside.lang = language
    aside = Aside.objects.all()
    if aside:
        aside = aside[0]

    Event.lang = language
    try:
        event = Event.objects.filter(draft=False).latest()
    except ObjectDoesNotExist:
        event = None

    Poll.lang = language
    try:
        poll = Poll.objects.filter(draft=False).latest()
    except ObjectDoesNotExist:
        poll = None

    translation.activate(language)
    return render_to_response('home/home.html', ({'language' : language,
                                                  'welcome' : welcome,
                                                  'candidate' : candidate,
                                                  'aside' : aside,
                                                  'event' : event,
                                                  'poll' : poll,}))

def donate(request, language):

    translation.activate(language)
    return render_to_response('home/donate.html', ({'language' : language,}))

def calendar(request, language):
    translation.activate(language)
    return render_to_response('home/calendar.html', ({'language' : language,}))

def join(request, language):
    translation.activate(language)
    return render_to_response('home/join.html', ({'language' : language,}))