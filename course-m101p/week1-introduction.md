# M101P · Week 1 · Introduction

Reading notes and homework of course [Week 1: Introduction](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_1_Introduction/).

## Homework

* Homework 1.1: Installed MongoDB, Python Virtual Environment, PyMongo driver and Bottle modules; restored the Mongo database `m101` from a [provided database dump](hw1-1.184820ec29b6.zip); performed a `db.hw1.findOne()`, returning a single document with the answer **42**
* Homework 1.2: ran the Python script [hw1.2-py](hw1-2.21394489c9ad.py) that connected to and retrieved the value **1815** from the DB
* Homework 1.3: ran Python Bottle script [hw1-3.py](hw1-3.e594fc84d4ac.py) that did the same, delivering the result **53** as the answer to an HTTP GET request on `http://localhost:8080/hw1/50`.

## Recap

Overview of MongoDB characteristics; install of MongoDB and intro to the Mongo shell; documents and intro to schema design; intro to the course project, a blog with posts, tags and comments; recap of JSON, the Python language (lists and dicts, iterating over those, functions, exceptions) and overview of the Bottle framework (see below); inserting a doc and handling exceptions with PyMongo.

Remember that Python dictionaries do not retain the order of their keys, whereas Javascript dictionaries do. For that reason, Pymongo idioms use arrays and tuples in some cases (sorting), rather than dictionaries.

Functions of the [Bottle Python framework](http://bottlepy.org/docs/dev/index.html) that were introduced: starting the listener ``bottle.debug``and ``bottle.run``, URL handlers ``bottle.route/get/post``, templates with arguments ``bottle.template`` (arg list or dict), handling form content ``bottle.post`` and ``bottle.request.forms.get``, using cookies ``bottle.request.get_cookie`` and ``bottle.response.set_cookie`` and redirecting ``bottle.redirect``.

Dans les exercices, ajouter `reloader=True` à l'instruction `bottle.run` dans `blog.py` pour qu'il recharge automatiquement les changements aux scripts (voir [Bottle Tutorial › Development › Autoreloading](http://bottlepy.org/docs/dev/tutorial.html#auto-reloading)):

    …
    bottle.debug( True)
    bottle.run( host='localhost', port=8082, reloader=True)
