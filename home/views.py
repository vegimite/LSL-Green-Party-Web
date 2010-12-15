# Create your views here.
from django.shortcuts import render_to_response
from django.utils import translation
from greenparty.home.models import Welcome, Candidate, Aside
from greenparty.news.models import Event


def home(request, language):
    welcome = Welcome.objects.all()[0]
    welcome.lang = language

    candidate = Candidate.objects.all()[0]
    candidate.lang = language

    aside = Aside.objects.all()[0]
    aside.lang = language

    event = Event.objects.filter(draft=False).latest('date')
    event.lang = language

    translation.activate(language)
    return render_to_response('home/home.html', ({'language' : language, 'welcome' : welcome, 'candidate' : candidate, 'aside' : aside, 'event' : event,}))

def donate(request, language):

    translation.activate(language)
    return render_to_response('home/donate.html', ({'language' : language,}))

def calendar(request, language):
    translation.activate(language)
    return render_to_response('home/calendar.html', ({'language' : language,}))

def join(request, language):
    translation.activate(language)
    return render_to_response('home/join.html', ({'language' : language,}))