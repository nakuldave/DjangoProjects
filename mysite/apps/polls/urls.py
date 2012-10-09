from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from apps.polls.views import *

urlpatterns = patterns('',
    url(r'^$', 'apps.polls.views.index'),
    url(r'^(?P<poll_id>\d+)/$', 'apps.polls.views.detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'apps.polls.views.results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'apps.polls.views.vote'),
)
