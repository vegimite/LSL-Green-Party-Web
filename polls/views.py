# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import translation
from django.views.generic.list_detail import object_list, object_detail
from polls.models import  Poll, Choice

def poll_vote(request, language, slug):

    if language == 'fr':
        p = get_object_or_404(Poll, slug_french=slug)
    else:
        p = get_object_or_404(Poll, slug_english=slug)

    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls.views.poll_detail', args=(language, slug)))

def poll_index(request, language):
    Poll.lang = language
    translation.activate(language)
    return object_list(request, Poll.objects.filter(draft=False), extra_context={'language':language, }, template_name='polls/poll_list.html', template_object_name='object')


def poll_detail(request, language, slug):
    Poll.lang = language
    translation.activate(language)

    if language == 'fr':
        slug_field = 'slug_french'
    else:
        slug_field = 'slug_english'

    return object_detail(request, Poll.objects.filter(draft=False), slug=slug, slug_field=slug_field, extra_context={'language':language, }, template_name='polls/poll_detail.html', template_object_name='poll')
