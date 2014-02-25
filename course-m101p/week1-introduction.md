# M101P · Week 1 · Introduction

Reading notes and homework of course [Week 1: Introduction](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_1_Introduction/).

## Recap of course contents

Overview of MongoDB characteristics; install of MongoDB and intro to the Mongo shell; documents and intro to schema design; intro to the course project, a blog with posts, tags and comments; recap of JSON, the Python language (lists and dicts, iterating over those, functions, exceptions) and overview of the Bottle framework (see below); inserting a doc and handling exceptions with PyMongo.

Functions of the [Bottle Python framework](http://bottlepy.org/docs/dev/index.html) that were introduced: starting the listener ``bottle.debug``and ``bottle.run``, URL handlers ``bottle.route/get/post``, templates with arguments ``bottle.template`` (arg list or dict), handling form content ``bottle.post`` and ``bottle.request.forms.get``, using cookies ``bottle.request.get_cookie`` and ``bottle.response.set_cookie`` and redirecting ``bottle.redirect``.

## Homework

Installed MongoDB, Python Virtual Environment, PyMongo driver and Bottle modules; restored a Mongo database from a dump; ran a Python script that connected to and retrieved a value from the DB; ran a Python Bottle script that did the same, delivering the result as the answer to an HTTP request.
