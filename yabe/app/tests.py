# -*- coding: utf-8 -*-

"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

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
# file:         tests.py
#
# function:     test cases
#
# description:  tests the model layer
#
# author:       Mohammed Safwat (MS)
#
# environment:  Kate 3.4.5, python 2.6.4, Fedora release 13 (Goddard)
#
# notes:        This is a private program.
#
############################################################

from app.models import Comment, Post, User
from django.core import management
from django.test import TransactionTestCase

class SimpleTest(TransactionTestCase):

    """Model tests"""

    def test_create_and_retrieve_user(self):
        """Test CRUD operations on users."""
        # Create a new user and save it
        User.objects.create(
            email="bob@gmail.com", password="secret", fullname="Bob")

        # Retrieve the user with e-mail address bob@gmail.com
        bob = User.objects.get(email="bob@gmail.com")

        # Test
        self.assertTrue(bob)
        self.assertEqual("Bob", bob.fullname)

    def test_create_post(self):
        """Test relations between users and posts."""
        # Create a new user and save it
        bob = User.objects.create(
            email="bob@gmail.com", password="secret", fullname="Bob")

        # Create a new post
        Post.objects.create(
            author=bob, title="My first post", content="Hello world")

        # Test that the post has been created
        self.assertEqual(1, Post.objects.count())

        # Tests
        # Retrieve all posts created by Bob
        try:
            firstPost = Post.objects.get(author=bob)
        except Post.DoesNotExist:
            self.fail()
        self.assertTrue(firstPost)
        self.assertEqual(bob, firstPost.author)
        self.assertEqual("My first post", firstPost.title)
        self.assertEqual("Hello world", firstPost.content)
        self.assertTrue(firstPost.postedAt)

    def test_full(self):
        """Test data from fixtures."""
        import_data_cmd = "loaddata"
        management.call_command(import_data_cmd, "data.yaml")

        # Count things
        self.assertEqual(2, User.objects.count())
        self.assertEqual(3, Post.objects.count())
        self.assertEqual(3, Comment.objects.count())

        # Try to connect as users
        self.assertTrue(User.connect("bob@gmail.com", "secret"))
        self.assertTrue(User.connect("jeff@gmail.com", "secret"))
        self.assertFalse(User.connect("jeff@gmail.com", "badpassword"))
        self.assertFalse(User.connect("tom@gmail.com", "secret"))

        # Find all of Bob's posts
        bobPosts = Post.objects.filter(author__email="bob@gmail.com")
        self.assertEqual(2, bobPosts.count())

        # Find all comments related to Bob's posts
        bobComments = \
            Comment.objects.filter(post__author__email="bob@gmail.com")
        self.assertEqual(3, bobComments.count())

        # Find the most recent post
        frontPost = Post.objects.latest("postedAt")
        self.assertTrue(frontPost)
        self.assertEqual("About the model layer", frontPost.title)

        # Check that this post has two comments
        self.assertEqual(2, frontPost.comment_set.count())

        # Post a new comment
        frontPost.addComment("Jim", "Hello guys")
        self.assertEqual(3, frontPost.comment_set.count())
        self.assertEqual(4, Comment.objects.count())

    def test_post_comments(self):
        """Test relations between posts and comments."""
        # Create a new user and save it
        bob = User.objects.create(
            email="bob@gmail.com", password="secret", fullname="Bob")

        # Create a new post
        bobPost = Post.objects.create(
            author=bob, title="My first post", content="Hello world")

        # Post a first comment
        Comment.objects.create(
            post=bobPost, author="Jeff", content="Nice post")
        Comment.objects.create(
            post=bobPost, author="Tom", content="I knew that !")

        # Retrieve all comments
        bobPostComments = Comment.objects.filter(post=bobPost)

        # Tests
        self.assertEqual(2, len(bobPostComments))

        firstComment = bobPostComments[0]
        self.assertTrue(firstComment)
        self.assertEqual("Jeff", firstComment.author)
        self.assertEqual("Nice post", firstComment.content)
        self.assertTrue(firstComment.postedAt)

        secondComment = bobPostComments[1]
        self.assertTrue(secondComment)
        self.assertEqual("Tom", secondComment.author)
        self.assertEqual("I knew that !", secondComment.content)
        self.assertTrue(secondComment.postedAt)

    def test_try_connect_as_user(self):
        """Test user credentials."""
        # Create a new user and save it
        User.objects.create(
            email="bob@gmail.com", password="secret", fullname="Bob")

        # Test
        self.assertTrue(User.connect("bob@gmail.com", "secret"))
        self.assertFalse(User.connect("bob@gmail.com", "badpassword"))
        self.assertFalse(User.connect("tom@gmail.com", "secret"))

    def test_use_the_comments_relation(self):
        """Test navigation from posts to comments."""
        # Create a new user and save it
        bob = User.objects.create(
            email="bob@gmail.com", password="secret", fullname="Bob")

        # Create a new post
        bobPost = Post.objects.create(
            author=bob, title="My first post", content="Hello world")

        # Post a first comment
        bobPost.addComment("Jeff", "Nice post")
        bobPost.addComment("Tom", "I knew that !")

        # Count things
        self.assertEqual(1, User.objects.count())
        self.assertEqual(1, Post.objects.count())
        self.assertEqual(2, Comment.objects.count())

        # Retrieve Bob's post
        bobPost = Post.objects.get(author=bob)
        self.assertTrue(bobPost)

        # Navigate to comments
        post_comments = bobPost.comment_set.all()
        self.assertEqual(2, len(post_comments))
        self.assertEqual("Jeff", post_comments[0].author)

        # Delete the post
        bobPost.delete()

        # Check that all comments have been deleted
        self.assertEqual(1, User.objects.count())
        self.assertEqual(0, Post.objects.count())
        self.assertEqual(0, Comment.objects.count())
