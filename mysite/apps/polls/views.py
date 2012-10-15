import inspect
from apps.polls.models import Poll,Choice
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.template import Context, loader,RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse

from pivotal import HttpSession
from django.core.cache import get_cache

def index(request):
    session = HttpSession(request)
    print session.getId()
    text = {'one':'one','t':'t'}
    if session.get('user') :        
        print inspect.stack()[0][3], session.get('user')
        print inspect.stack()[0][3], session.get('test')
    else :
        session.set('user', request.user)
        session.set('test', text)

    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))

def detail(request, poll_id):
    session = HttpSession(request)
    session.delete('testtttt')
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p},context_instance=RequestContext(request))
    #	p = get_object_or_404(Poll, pk=poll_id)
    #	return render_to_response('polls/detail.html', {'poll': p})
    #    try:
    #        p = Poll.objects.get(pk=poll_id)
    #    except Poll.DoesNotExist:
    #        raise Http404
    #    return render_to_response('polls/detail.html', {'poll': p})

def results(request, poll_id):
    cache = get_cache('default')
    if cache.get('user') :        
        print inspect.stack()[0][3], cache.get('user')
    else :
        cache.set('user', request.user, 30000)

    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})

def vote(request, poll_id):
    cache = get_cache('default')
    if cache.get('user') :        
        print inspect.stack()[0][3], cache.get('user')
    else :
        cache.set('user', request.user, 30000)

    p = get_object_or_404(Poll, pk=poll_id)
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
        return HttpResponseRedirect(reverse('apps.polls.views.results', args=(p.id,)))