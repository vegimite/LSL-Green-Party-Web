# Create your views here.
from django.shortcuts import render_to_response
from greenparty.home.models import Welcome


def home(request, language):
   # page = HomePage.objects.all()[0]
    #page.lang = language
    return render_to_response('home/home.html', ({'language' : language,}))

def about(request, language):
    contacts = Contact.objects.all()
    return render_to_response('home/about.html', ({'contacts' : contacts, 'language' : language,}))