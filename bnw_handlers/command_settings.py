# -*- coding: utf-8 -*-
#from twisted.words.xish import domish

from base import *
from bnw_core.base import config
import random

import bnw_core.bnw_objects as objs

class SimpleSetting(object):
    def __init__(self,default=None):
        self.default = default

    def get(self,request,name):
        setts = request.user.get('settings',{})
        return setts.get(name,self.default)

    @defer.inlineCallbacks
    def write(self,request,name,value):
        if len(value)>2048:
            defer.returnValue((False,('%s value is too long.' % (name,))))
        _ = yield objs.User.mupdate({'name':request.user['name']},
                    {'$set':{'settings.'+name:value}},safe=True)
        defer.returnValue((True,))

class ServiceJidSetting(SimpleSetting):
    def get(self,request,name):
        setts = request.user.get('settings',{})
        return setts.get(name,config.srvc_name)
    def write(self,request,name,value):
        return SimpleSetting.write(self,request,name,request.to)

class HttpsLinksSetting(SimpleSetting):
    def write(self, request, name, value):
        if value not in ['on', 'off']:
            return (False, ("Value can only be 'on' or 'off'"))
        else:
            return super(HttpsLinksSetting, self).write(request, name, value)

optionnames = {
    'usercss': SimpleSetting(),
    'password': SimpleSetting(),
    'servicejid': ServiceJidSetting(),
    'httpslinks': HttpsLinksSetting('off'),
}

@require_auth
@defer.inlineCallbacks
def cmd_set(request, **kwargs):
    """ Настройки """
    if not kwargs:
        # Show current settings.
        current = {}
        for n,v in optionnames.iteritems():
            current[n]=v.get(request,n)
        defer.returnValue(
            dict(ok=True,format='settings',settings=current))
    else:
        if 'name' in kwargs:
            # Simplified interface.
            name, value = kwargs['name'], kwargs['value']
        else:
            # Redeye interface.
            name, value = kwargs.items()[0]
        if not name in optionnames:
            defer.returnValue(
                dict(ok=False,desc='Unknown setting: %s' % kwargs['name']))
        else:
            res = yield optionnames[name].write(request, name, value)
            if not res[0]:
                defer.returnValue(
                    dict(ok=False,desc=res[1])
                )
        defer.returnValue(
            dict(ok=True,desc='Settings updated.'))
