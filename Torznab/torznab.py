# Author: Dennis Lutter <lad1337@gmail.com>
# URL: https://github.com/lad1337/XDM
#
# This file is part of XDM: eXtentable Download Manager.
#
# XDM: eXtentable Download Manager. Plugin based media collection manager.
# Copyright (C) 2013  Dennis Lutter
#
# XDM is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# XDM is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.

from xdm.plugins import *
from collections import OrderedDict
from xdm import helper

class Torznab(Indexer):
    version = "0.1"
    identifier = "org.legocloud.torznab"

    _config = OrderedDict([('host', 'http://nzbs2go.com'),
                           ('apikey', '')
                           ])
    types = ['de.lad1337.torrent']

    def _baseUrl(self, host, port=None):
        if not host.startswith('http'):
            host = 'http://%s' % host
        if port:
            return "%s:%s/" % (host, port)
        if host.endswith('/'):
            return "%s" % host
        else:
            return "%s/" % host

    def _baseUrlApi(self, host, port=None):
        return "%sapi&apikey=" % (self._baseUrl(host, port), self.c.apikey)

    def searchForElement(self, element):
        # payload = {'apikey': self.c.apikey,
        #            't': 'search',
        #            'maxage': self.c.retention,
        #            'cat': self._getCategory(element),
        #            'o': 'json'
        #            }

        # downloads = []
        terms = element.getSearchTerms()
        for term in terms:
            log("Torznab final search for term %s url %s" % (term, self._baseUrlApi(self.c.host, self.c.port)))

    def _testConnection(self):
        log("Torznab API %s" % self._baseUrlApi(self.c.host, self.c.port))

    config_meta = {
        'plugin_desc': 'Generic Torznab indexer. Categories are there numerical id of Torznab, use "Get categories"',
        'plugin_buttons': {'test_connection': {'action': _testConnection, 'name': 'Test connection'}},
        }