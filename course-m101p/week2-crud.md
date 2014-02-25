# M101P · Week 2 · CRUD

Reading notes and homework related to course [Week 2: CRUD](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_2_CRUD/) .

## Recap

* CRUD is IFUR: `insert()`, `find()`, `update()`, `remove()`
* 1. **sort** 2. **skip** 3. **limit**
* `.find(…).pretty()` displays results in a more human readable form
* Recap on JS properties and dictionary lookup
* Data is stored in [BSON](http://bsonspec.org) format in MongoDB, which is a superset of JSON, having namely _ObjectId_, _date_, _integer 32/64_ and _binary_ types
* MongoDB Shell command-line editing hints; the _shell_ has support for the various MongoDB types: `Date()` (gets converted to `ISODate()` automatically), `NumberInt()`, `NumberLong()` for instance
* ObjectId is a UUID; each doc must have a PK, which is immutable in the DB
* Inserting
* Finding: `find()`, `findOne()`, excluding fields from output, specifying query by example; for instance: `db.scores.find({ type: "essay", score: 50}, { student: true, _id: false})`
* All search ops are strongly typed and dynamically typed; when using polymorphic field contents, beware! such searches can be refined with `$type` (for instance, `.find( { name: { $type: 2 } })` with _type_ according to [BSON spec](http://bsonspec.org/#/specification) of element types; type 2 being a string) and `$exists`(for instance, `.find( { profession: { $exists: true | false }})`)
* Querying for string patterns with regular expressions: `.find( { name: { $regex: "e$" }} )`; regular expressions tend not to be efficiently optimized, except a few cases, such as expressions starting with a caret (for instance, `$regex: "^A"`)
* Combining the operators: `db.users.find({"name": {$regex: "q"}, "email": {$exists: true}})`
* Combining expressions with `$or: [ …, …]` and `$and: [ …, …]`: `db.scores.find({ $or: [ { score: { $lt: 50}}, { score: { $gt: 90}} ] })`
* Beware! Javascript will silently parse the following, although it is probably an incomplete query expression: `db.scores.find( { score: { $lt: 50}}, { score: { $gt: 90}})` will return all documents with score greater than 90 – the second property definition replaces the first
* Querying arrays: matching is polymorphic over arrays (top level only); `db.products.find( { tags: "shiny"})` would match `{ _id: 42, name: "wiz-o-matic", tags: [ "awesome", "shiny", "green"]}` as well as `{ _id: 42, name: "snap-o-lux", tags: "shiny"}`
* Querying for all given values with `$all: [ …, …]`: `db.accounts.find( { favorites: { $all: [ "pretzels", "beer"] }})` the array values have to be a subset of the values of the field that is queried for, in any order
* Querying for any of the given values with `$in: […, …]`: `db.accounts.find( { name: { $in: [ "Howard", "John" ]}})`
* Combining both `$all` and `$in`: `db.users.find( { friends: { $all: [ "Joe" , "Bob" ] }, favorites: { $in: [ "running" , "pickles" ]}})` will match `{ name : "Cliff" , friends : [ "Pete" , "Joe" , "Tom" , "Bob" ] , favorites : [ "pickles", "cycling" ] }`

## Homework

* [Homework 2.1](hw2-1-answer.md) Find all exam scores greater than or equal to 65, and sort those scores from lowest to highest  `db.grades.find( { "score": { $gte: 65}}).sort( { "score": 1})`
* [Homework 2.2](hw2-2-answer.md) Identity of the student with the highest average in the class
* [Homework 2.3](hw2-3-answer.md) Adapt `userDAO.py` to add a new user upon sign-up and validate a login by retrieving the right user document.
