# MongoDB Course M101P

Courseware, homework and resources related to the course [M101P: MongoDB for Developers](https://education.mongodb.com/courses/10gen/M101P/2014_February/info).

## Notes and homework

* [Week 4: Performance](week4-performance.md)
* [Week 3: Schema Design](week3-schema.md)
* [Week 2: CRUD](week2-crud.md)
* [Week 1: Introduction](week1-introduction.md)

## Courseware

Access to these links requires an account and login to the MongoDB University website.

* [Course info](https://education.mongodb.com/courses/10gen/M101P/2014_February/info) overview and news
* [Course wiki](https://education.mongodb.com/courses/10gen/M101P/2014_February/wiki/M101P-Feb-2014/) links to all videos on YouTube
* [Course forum](https://education.10gen.com/courses/10gen/M101P/2014_February/discussion/forum) 

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

Restoring the database from a dump:

    $ cd course-m101p
    $ wget https://education.mongodb.com/static/10gen_2014_M101P_February/handouts/hw1-1.184820ec29b6.zip
    $ unzip hw1-1.184820ec29b6.zip
    $ restoremongo dump

Importing content of a database from a JSON file:

    $ mongoimport -d students -c grades < grades.ef42a2b3e7ff.json
    connected to: 127.0.0.1
    Tue Feb 18 15:44:34.158 check 9 800
    Tue Feb 18 15:44:34.158 imported 800 objects
