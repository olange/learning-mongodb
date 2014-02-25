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
* All search ops are strongly typed and dynamically typed; when using polymorphic field contents, beware! such searches can be refined with `$type` (for instance, `.find( { name: { $type: 2 } })` with _type_ according to [BSON spec](http://bsonspec.org/#/specification) of element types; type 2 being a string) and `$exists`(for instance, `.find( { profession: { $exists: true | false }})`)
* Querying for string patterns with regular expressions
* 1. **sort** 2. **skip** 3. **limit**

## Homework

* [Homework 2.1](hw2-1-answer.md) Find all exam scores greater than or equal to 65, and sort those scores from lowest to highest  `db.grades.find( { "score": { $gte: 65}}).sort( { "score": 1})`
* [Homework 2.2](hw2-2-answer.md) Identity of the student with the highest average in the class
* [Homework 2.3](hw2-3-answer.md) Adapt `userDAO.py` to add a new user upon sign-up and validate a login by retrieving the right user document.
