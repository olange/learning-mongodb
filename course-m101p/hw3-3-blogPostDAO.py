__author__ = 'aje'


#
# Copyright (c) 2008 - 2013 10gen, Inc. <http://10gen.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

import sys
import re
import datetime
from pymongo import DESCENDING

# The Blog Post Data Access Object handles interactions with the Posts collection
class BlogPostDAO:

    # constructor for the class
    def __init__(self, database):
        self.db = database
        self.posts = database.posts

    # inserts the blog entry and returns a permalink for the entry
    def insert_entry(self, title, post, tags_array, author):
        print "inserting blog entry", title, post

        # fix up the permalink to not include whitespace

        exp = re.compile('\W') # match anything not alphanumeric
        whitespace = re.compile('\s')
        temp_title = whitespace.sub("_",title)
        permalink = exp.sub('', temp_title)

        # Build a new post
        post = {"title": title,
                "author": author,
                "body": post,
                "permalink":permalink,
                "tags": tags_array,
                "comments": [],
                "date": datetime.datetime.utcnow()}

        # now insert the post
        try:
            # XXX HW 3.2 Work Here to insert the post
            self.posts.insert( post, j=True)
            print "Inserting the post"
        except:
            print "Error inserting post"
            print "Unexpected error:", sys.exc_info()[0]

        return permalink

    # returns an array of num_posts posts, reverse ordered
    def get_posts(self, num_posts):

        # XXX HW 3.2 Work here to get the posts
        cursor = self.posts.find().sort([( "date", DESCENDING)]).limit( num_posts)

        l = []

        for post in cursor:
            post['date'] = post['date'].strftime("%A, %B %d %Y at %I:%M%p") # fix up date
            if 'tags' not in post:
                post['tags'] = [] # fill it in if its not there already
            if 'comments' not in post:
                post['comments'] = []

            l.append({'title':post['title'], 'body':post['body'], 'post_date':post['date'],
                      'permalink':post['permalink'],
                      'tags':post['tags'],
                      'author':post['author'],
                      'comments':post['comments']})

        return l


    # find a post corresponding to a particular permalink
    def get_post_by_permalink(self, permalink):

        # XXX Work here to retrieve the specified post
        post = self.posts.find_one( { "permalink": permalink })

        if post is not None:
            # fix up date
            post['date'] = post['date'].strftime("%A, %B %d %Y at %I:%M%p")

        return post

    # add a comment to a particular blog post
    def add_comment(self, permalink, name, email, body):

        comment = {'author': name, 'body': body}

        if (email != ""):
            comment['email'] = email

        try:
            # XXX HW 3.3 Work here to add the comment to the designated post
            self.posts.update( { "permalink": permalink}, \
                               { "$push": { "comments": comment }})
            last_error = db.runCommand({"getLastError":1})
            return last_error['n']          # return the number of documents updated

        except:
            print "Could not update the collection, error"
            print "Unexpected error:", sys.exc_info()[0]
            return 0








