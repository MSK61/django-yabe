# -*- coding: utf-8 -*-

############################################################
#
# Copyright 2010, 2014 Mohammed El-Afifi
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
# file:         urls.py
#
# function:     URLconf
#
# description:  dispatches URL patterns to callback view functions
#
# author:       Mohammed Safwat (MS)
#
# environment:  Kate 3.4.5, python 2.6.4, Fedora release 13 (Goddard)
#
# notes:        This is a private program.
#
############################################################

from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^yabe/', include('yabe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^$', 'views.index')
)

if settings.DEBUG:  # Serve static resources during development.
    urlpatterns += patterns('', (r'^' + settings.MEDIA_URL + r'(.+)$',
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
