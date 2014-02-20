# MongoDB Course M101P

Courseware, homework and resources related to the course [M101P: MongoDB for Developers](https://education.mongodb.com/courses/10gen/M101P/2014_February/info).

## Courseware

 * [Course info](https://education.mongodb.com/courses/10gen/M101P/2014_February/info) overview and news
 * [Course wiki](https://education.mongodb.com/courses/10gen/M101P/2014_February/wiki/M101P-Feb-2014/) links to all videos on YouTube
 * [Course forum](https://education.10gen.com/courses/10gen/M101P/2014_February/discussion/forum) discussions about the course
 * [Week 2: CRUD](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_2_CRUD/)
 * [Week 1: Introduction](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_1_Introduction/)

## Running

Start MongoDB:

    $ cd course-m101p
    $ mongod --dbpath=data/db/ &

Activate the Python Virtual Environment:

    $ source venv/bin/activate

Start the Mongo shell

    $ mongo

To deactivate the Python Virtual Environment:

    $ deactivate

## Installing

### Generic Python install for Mac OS X

XCode Command Line Tools:

    $ xcode-select --install

Mongo:

    $ brew install mongodb

PIP:

    $ sudo easy_install pip

Python Virtual Env:

    $ sudo pip install virtualenv
    $ virtualenv --distribute venv

### Course specific installs

PyMongo and Bottle modules for Python:

    $ cd course-m101p
    $ source venv/bin/activate
    $ pip install pymongo
    $ pip install bottle

Restoring the database:

    $ cd course-m101p
    $ wget https://education.mongodb.com/static/10gen_2014_M101P_February/handouts/hw1-1.184820ec29b6.zip
    $ unzip hw1-1.184820ec29b6.zip
    $ restoremongo dump
