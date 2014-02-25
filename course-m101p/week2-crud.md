# M101P · Week 2 · CRUD

Reading notes and homework related to course [Week 2: CRUD](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_2_CRUD/) .

## Recap

* CRUD is IFUR: `insert()`, `find()`, `update()`, `remove()`.
* Recap on JS properties and dictionary lookup
* Data is stored in [BSON](http://bsonspec.org) format in MongoDB, which is a superset of JSON, having namely _ObjectId_, _date_, _integer 32/64_ and _binary_ types
* MongoDB Shell command-line editing hints; the _shell_ has support for the various MongoDB types: `Date()` (gets converted to `ISODate()` automatically), `NumberInt()`, `NumberLong()` for instance
* ObjectId is a UUID; each doc must have a PK, which is immutable in the DB
* Inserting
* Finding: `find()`, `findOne()`, excluding fields from output, specifying query by example
* All search ops are strongly typed and dynamically typed; when using polymorphic field contents, beware! such searches can be refined with `$type` () and `$exists`
* Querying for string patterns with regular expressions

## Homework

* (à compléter)
