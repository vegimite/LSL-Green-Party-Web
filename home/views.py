# Create your views here.
from django.shortcuts import render_to_response
from django.utils import translation
from greenparty.home.models import Welcome, Candidate


def home(request, language):
    welcome = Welcome.objects.all()[0]
    welcome.lang = language

    candidate = Candidate.objects.all()[0]
    candidate.lang = language

    translation.activate(language)
    return render_to_response('home/home.html', ({'language' : language, 'welcome' : welcome, 'candidate' : candidate,}))

def donate(request, language):

    translation.activate(language)
    return render_to_response('home/donate.html', ({'language' : language,}))