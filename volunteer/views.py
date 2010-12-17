# Create your views here.
from django.shortcuts import render_to_response
from django.utils import translation
from django.http import HttpResponseRedirect
from greenparty.volunteer.models import Volunteer, Blurb, VolunteerForm

def volunteer(request, language):


    if request.method == 'POST': # If the form has been submitted...
        form = VolunteerForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass

            form.save()

            return HttpResponseRedirect('thanks/') # Redirect after POST
    else:
        form = VolunteerForm() # An unbound form

    Blurb.lang = language
    introtext = Blurb.objects.all()[0]

    translation.activate(language)
    return render_to_response('volunteer/volunteer.html', ({'language' : language, 'introtext' : introtext, 'form': form, }))

def thanks(request, language):
    translation.activate(language)
    return render_to_response('volunteer/thanks.html', ({'language' : language, }))