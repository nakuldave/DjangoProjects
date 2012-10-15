# -*- coding: utf-8 -*-
"""models.py: Simple History Middleware - sued for capturing the user"""

__author__    = 'Marty Alchin'
__date__      = '2011/08/29 20:43:34'
__credits__   = ['Marty Alchin', 'Corey Bertram', 'Steven Klass']

from django.db.models import signals
from django.utils.functional import curry
from django.utils.decorators import decorator_from_middleware

def new_method(self):
    return "Rajesh from new method"


class CurrentSessionMiddleware(object):

    def process_request(self, request):
        if request.method in ['HEAD', 'OPTIONS', 'TRACE']:
            # We aren't doing anything return..
            return

        if hasattr(request, 'user') and request.user.is_authenticated:
            user = request.user
        else:
            user = None

        print "----26-----",user
   

    

#record_current_user = decorator_from_middleware(CurrentSessionMiddleware)