# Create your views here.
from django.shortcuts import render_to_response
from greenparty.volunteer.models import Volunteer, VolunteerBlurb

def volunteer(request, language):


    introtext = VolunteerBlurb.objects.all()[0]
    introtext.lang = language

    return render_to_response('volunteer/volunteer.html', ({'language' : language, 'introtext' : introtext }))