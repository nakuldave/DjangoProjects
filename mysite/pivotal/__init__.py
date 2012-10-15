# -*- coding: utf-8 -*-

__author__    = 'Rajesh'
__date__      = '2011/08/29 20:43:34'
__credits__   = ['Rajesh Pappula', 'Steven Klass']

from django.core.cache import get_cache


class HttpSession(object):
    """A basic HTTP session."""

    def __init__(self,request=None):
        self.cache = get_cache('default')
        if request :
            self.sessionid = request.COOKIES['sessionid']
            self.cache.key_prefix = self.sessionid
        
    def set(self,key,value):
        return self.cache.set(key,value)
        
    def set_many(self,key_value_dict):
        return self.cache.set_many(key_value_dict)
        
    def delete(self,keys):
        return self.cache.delete_many(keys)
        
    def delete_many(self,key):
        return self.cache.delete(key)
    
    def getId(self):
        return self.sessionid
        
    def get(self,key):
        return self.cache.get(key)
        
    
    
    
        
    
    
    def contains(self,key):
        return self.cache.__contains__(key)

    

    