# -*- coding: utf-8 -*-

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
# file:         models.py
#
# function:     model layer
#
# description:  contains model classes
#
# author:       Mohammed Safwat (MS)
#
# environment:  Kate 3.4.5, python 2.6.4, Fedora release 13 (Goddard)
#
# notes:        This is a private program.
#
############################################################

from django.db import models

# Create your models here.
class User(models.Model):

    """Post author"""

    email = models.CharField(max_length=200)

    password = models.CharField(max_length=200)

    fullname = models.CharField(max_length=200)

    isAdmin = models.BooleanField()

    @staticmethod
    def connect(email, password):
        """Retrieve the user with the given email and password.

        `email` is the claimed user identity.
        `password` is the secret proving the user's identity.

        """
        try:
            return User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            return None

class Post(models.Model):

    """Article written by an author"""

    title = models.CharField(max_length=200)

    postedAt = models.DateTimeField(auto_now_add=True)

    content = models.TextField()

    author = models.ForeignKey(User)

    def addComment(self, author, content):
        """Add a comment to this post.

        `author` is the author of the comment to be added.
        `content` is the text of the comment to be added.

        """
        self.comment_set.create(post=self, author=author, content=content)
        return self

class Comment(models.Model):

    """Comment added to a post"""

    author = models.CharField(max_length=200)

    postedAt = models.DateTimeField(auto_now_add=True)

    content = models.TextField()

    post = models.ForeignKey(Post)
