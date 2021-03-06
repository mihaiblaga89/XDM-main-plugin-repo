# Author: Dennis Lutter <lad1337@gmail.com>
# URL: https://github.com/lad1337/XDM-main-plugin-repo/
#
# This file is part of a XDM plugin.
#
# XDM plugin.
# Copyright (C) 2013  Dennis Lutter
#
# This plugin is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This plugin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.

from xdm.plugins import *

class Replace(SearchTermFilter):
    version = "0.2"
    _config = {'replace_this': '&;:;/;|',
               'with_this': "; ;; "}
    config_meta = {'plugin_desc': 'Replace each item with another one for each search term. Separate by a ; (semicolon). This is case sensitive and whitespace is NOT striped'}

    def compare(self, element, terms):
        badList = self.c.replace_this.split(';')
        replaceList = self.c.with_this.split(';')
        if len(badList) != len(replaceList):
            log.warning('The two config fields from %s do not match in length check your ->;' % self)
            return terms
        replaceDict = {}
        for index, badThing in enumerate(badList):
            replaceDict[badThing] = replaceList[index]

        out = list(terms)
        for t in terms:
            out.append(replace_x(t, replaceDict))
        return out
