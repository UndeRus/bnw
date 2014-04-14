# -*- coding: utf-8 -*-
# from twisted.words.xish import domish

from base import *

import bnw.core.bnw_objects as objs


@require_auth
def cmd_interface(request, iface=None):
        """ Переключение интерфейса

        Переключение парсера команд xmpp-интерфейса.

        redeye: interface simplified
        simple: INTERFACE redeye"""
        parsers = ('simplified', 'redeye')
        if not iface:
            return dict(ok=True, desc='Possible interfaces: ' + ', '.join(parsers))
        if iface in parsers:
            request.user['interface'] = iface
            objs.User.save(request.user)
            return dict(ok=True, desc='Interface changed.')
        else:
            return dict(ok=False, desc='No such interface.')
