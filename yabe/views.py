# -*- coding: utf-8 -*-

"""displays the root page"""

############################################################
#
# Copyright 2010 Mohammed El-Afifi
# This file is part of yabe.
#
# yabe is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# yabe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with yabe.  If not, see <http://www.gnu.org/licenses/>.
#
# program:      yet another blog engine
#
# file:         views.py
#
# function:     root view
#
# description:  displays the site root page
#
# author:       Mohammed Safwat (MS)
#
# environment:  Kate 3.4.5, python 2.6.4, Fedora release 13 (Goddard)
#
# notes:        This is a private program.
#
############################################################

from django import shortcuts
def index(request):
    """Display the site root page.

    `request` is the request invoking this view.

    """
    return shortcuts.render_to_response('index.html')
