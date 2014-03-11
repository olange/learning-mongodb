# M101P · Week 4 · Performance

Notes and homework related to [Week 4: Performance](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_4_Performance/). 3 hours 45 min. of videos and notes, 45 min. of homework.

## Homework

* [Homework 4.1](hw4-1-answer.md) Which of the following queries can utilize an index?
* [Homework 4.2](hw4-2-answer.md) What can you infer from the following `explain` output? 
* [Homework 4.3](hw4-3-answer.md) Making the blog fast
* [Homework 4.4](hw4-4-answer.md) Analyze a profile log taken from a mongoDB instance

## Recap

### Indexes

* Creating an index: `db.students.ensureIndex({ student_id: 1, class: -1})` puts a composite index on field `student_id`, in ascending order, and on field `class`, in descending order; order has no effect on searching, but makes a difference when sorting on these fields
* Finding indexes: all with `db.system.indexes.find()`; for a given collection with `db.students.getIndexes()`
* Dropping an index: `db.students.dropIndex({ student_id: 1})`
* Multikey indexes: automatically created when inserting an array in a field participating in an index; for compound indexes, only one of the fields participating in the index can be an array (Mongo cannot index parallel arrays); multikey indexes can be defined for subdocuments also: `db.people.ensureIndex( {"adresses.tag": 1})`
* Creating unique indexes: `db.students.ensureIndex({ student_id: 1}, { unique: true})`
* … and removing duplicate keys: `db.students.ensureIndex({ student_id: 1}, { unique: true, dropDups: true})`; be very careful: there is No Way to determine which of the duplicates keys will be removed; and the removed documents are gone forever
* Sparse indexes: if the key of an index is missing within a document, it maps to Null; if the index is unique, there can be only one null; it is however possible to create sparse indexes, that index only keys being set: `db.products.ensureIndex({ size: 1}, { [unique: true,] sparse: true})`; **beware**: when sorting on the key of a sparse index, documents without an entry won't appear in the results! it is an artifact of the sparse index, which gets used by the sort, therefore changing its semantics
* Creating indexes in the background: by default, indexes are created in the foreground, which is faster, but is blocking all writers; with `db.people.ensureIndex( {…}, { background: true})`, it will be created in the background, not blocking other writers, however being slower; in a replica set, one server can be pulled out of the set to be indexed, and then put back again; a mongod instance can only build one background index at a time per database

### Explain

* `db.foo.find({c:1}).explain()`
* `"cursor": "BasicCursor"` --> full collection scan
* `"millis": 3` --> time taken
* `"cursor": "BtreeCursor a_1_b_1_c_1"` --> index `a_1_b_1_c_1` was used
* `"isMultiKey": false` --> none of the values are arrays
* `"n": 1` --> number of documents returned
* `"nscannedObjects": 1` --> number of documents that were scanned
* `"nscanned": 1` --> number of documents or index entries that were scanned
* `"indexBounds": [  …]` --> strategy followed and boundary values
* `"indexOnly": false` --> `true` if everything queryied for is satisfied by the index, without retrieving the actual document

### Considerations about indexes

* **When is an index used**? When there are many indexes available for a query, MongoDB runs different _query plans_ in parallel with the different indexes, and memorizes the one that returned first; this happens automatically behind the scenes; every hundred or so queries, it will forget what it learned and start over.
* **Index Size**: if an index can be kept in memory, it is blazing fast; use `db.students.stats()` to see how much place the data takes on disk; `db.students.totalIndexSize()` to see how much place the indexes take
* **Index cardinality**: in _regular indexes_, there is an index point for every key (#index points --1:1-- #documents); in _sparse indexes_, there could be less index points than documents, as null keys are dropped (#index points <= # documents); in _multikey documents_, there could be more index points than documents, as we have one for each value in arrays (#index points > #documents)
* **Index selectivity**: have them be very selective if possible, it improves performance; for instance, in a logging collection, with millions of documents having a timestamp and opcode, where the opcode represents a small set of operations, it is best to create an index on `(timestamp, opcode)` rather than `(opcode, timestamp)`, because queries on a time interval with the first index will eliminate 4/5 of the collection's data upfront, leaving only 1/5 documents to scan within on the opcode
* **Providing hints** to the database: `db.foo.find().hint({ a:1, b:1, c:1})`; or `.hint( "$natural": 1)` to use no index (the «natural index») and have a cursor that goes thru all documents
* … in Pymongo: `doc = db.foo.find(query).hint( [ ("c", pymongo.ASCENDING)])` (providing an array of tuples, as dictionaries are not ordered in Python -- as they are in Javascript and JSON)
* **Efficiency of index use**: `$gt`, `$lt`, `$ne` operators are not particulary efficient to use with an index, as they leave a lot of documents to go thru; the same for regexps, which require generally to go thru all documents -- to the exception of `^abc` regexps (matches strings _starting with_ "abc"); so it is important to not only consider if and which index was used for a query, but also how it was used, if the database still had to go thru millions of documents

### Geospatial indexes

* What is the location closest to an (x,y) point? `db.places.ensureIndex({ location: "2d"})`
* Finding with `db.places.find({ location: { "$near": [ x, y]}})`; will be return by order of increasing distance, so add a limit `.limit( 3)`
* To have geospatial indexes considering the curvature of the earth, in a _spherical space model_: you still create the index with `.ensureIndex({ stores: "2d"})`, but run a query with `db.runCommand({ geoNear: "stores"}, near:[ long, lat], spherical: true, maxDistance: rad})` -- order of the tuple (long, lat) matters, _longitude_ comes first, then _latitude_

### Logging and Profiling

* **Log slow queries** is built in: above 100ms, Mongo automatically writes an entry within its logs (console or logfiles)
* **Profiler** levels: 0 = off; 1 = log slow queries; 2 = log all queries (debugging)
* Start _mongod_ with `mongod --dbpath … --profile 1 --slowms 2` to have Mongo automatically profile slow queries running more than 2ms
* Use `db.system.profile.find()` to see what was logged; note `db.system.profile` is a capped-collection, which rotates its contents
* Use `db.system.profile.find({ ns:/school.students/}).sort({ ts: 1})` to find queries on collection `students` within DB `school`, sorting by the timestamp
* Use `db.system.profile.find({ millis: { $gt: 1}}).sort({ ts: 1})` to find queries that were slower than 1ms
* Turning the profiler from the Mongo shell: `db.getProfilingLevel()` to read the level, `db.getProfilingStatus()` to read the status, `db.setProfilingLevel( 1, 4)` to set profiling level to 1 and look for slow queries longer than 4ms; `db.setProfilingLevel( 0)` to turn it off
* **Mongostat**: most looked information is `idx miss %` --> index miss rate in memory, percentage of queries where Mongo has to go to disk; beware when it says 0: consider if either the query uses no index at all, or it resides entirely in memory
* **Mongotop**: high-level view of where Mongo is spending its time; `mongotop 3` will display how much time MongoDB spent accessing/updating each collection in the repeating interval of the last 3 seconds

### Sharding

* _Sharding_ is a technique for splitting up a large collection among multiple servers; in front of multiple `mongod` sharded servers, there is a `mongos` server, which is a router; the application accesses this `mongos` server
* About architecture: The `mongos` server is often _colocated_ on the same machine as the _app server_. There can be _many_ `mongos` servers.
* Then, the `mongod` servers are generally on different physical servers, and each of them can -- it is recommended -- be part of a _replicat set_, that is, another group of `mongod` servers, where data is kept in sync, so that if one server goes down, no data is lost; the _replica set_ can be looked at as _one shard_
* Mongo shards according to a _shard key_; when performing queries and updates, the shard key will be used to sent them to the right system
* An _insert_ must include the shard key (the entire shard key if it's a compound key) to complete; so the developer has to be aware of what the shard key is
* For _find/update/remove_ operations, to get higher performance, the shard key should be specified, if one knowns it; otherwise, `mongos` will have to broadcast the queries to the `mongod` servers, which will keep each of them busy
* By the way, _updates_ on sharded collections should be made _multi_
* Choosing a shard key is a topic in itself.

### Review

* Indexes are critical to performance 
* Explain command to look how the database uses the indexes for particular queries
* Hint command to instruct the database which particular index to use
* Profiling to figure out which queries are slow, then use explain and hinting to improve them, possibly create new indexes.
