# -*- coding: utf-8 -*-

"""main application package"""

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
# file:         __init__.py
#
# function:     application package export file
#
# description:  performs application initialization
#
# author:       Mohammed Safwat (MS)
#
# environment:  Kate 3.4.5, python 2.6.4, Fedora release 13 (Goddard)
#
# notes:        This is a private program.
#
############################################################

from app import models
from django.core.management import call_command

_IMPORT_CMD = "loaddata"
_SYNC_DB_CMD = "syncdb"

# Create the database if it doesn't exist.
call_command(_SYNC_DB_CMD, interactive=False)

# Check if the database is empty
if not models.User.objects.exists():
    call_command(_IMPORT_CMD, "initial-data.yaml")
