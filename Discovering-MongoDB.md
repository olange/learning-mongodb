# Discovering MongoDB

### Documentation

* [MongoDB 2.4 Manual](http://docs.mongodb.org)
* [MongoDB Quick Reference Cards](https://www.mongodb.com/reference)

### Courses and Tutorials

* [Course M101P «MongoDB for developers»](../tree/master/course-m101p)
* [Webminar «Building an application with MongoDB»](../tree/master/webinar-build-an-app)

### Channels

* [Geneva MongoDB User Group](http://genevamug.ch)
* [MongoDB User Google Group](https://groups.google.com/forum/#!forum/mongodb-user)
* Twitter: [#MongoDBBasics](https://twitter.com/search?q=%23MongoDBBasics) [@MongoDB](https://twitter.com/MongoDB)

### Articles

* [Call me maybe: MongoDB](http://aphyr.com/posts/284-call-me-maybe-mongodb)
* [MongoDB schema design pitfalls](https://blog.serverdensity.com/mongodb-schema-design-pitfalls/)
* [Analyze Performance of Database Operations](http://docs.mongodb.org/manual/tutorial/manage-the-database-profiler/) enable with `db.setProfilingLevel(2)` and query with `db.system.profile.find( { millis : { $gt : 5 } } ).pretty()` for instance; `show profile` displays the five most recent events that took more than 1ms
* [Measuring time and analyzing a query: explain()](http://docs.mongodb.org/manual/reference/method/cursor.explain/) `db.collection.find().explain().millis` gives the time taken by a given query
* [Ways to implement data versioning in MongoDB](http://stackoverflow.com/questions/4185105/ways-to-implement-data-versioning-in-mongodb) StackOverflow
* [Atomic Counters using MongoDB’s findAndModify with PHP](http://chemicaloliver.net/programming/atomic-counters-using-mongodbs-findandmodify-with-php/)
* [How to apply automatic versioning to a C# class](http://stackoverflow.com/questions/20351698/how-to-apply-automatic-versioning-to-a-c-sharp-class)
* [Data Models](http://docs.mongodb.org/manual/data-modeling)
* [Use Case: Metadata and Asset Management](http://docs.mongodb.org/ecosystem/use-cases/metadata-and-asset-management/) describes the design and pattern of a content management system using MongoDB modeled on the popular Drupal CMS
* [Use Case: Storing comments](http://docs.mongodb.org/ecosystem/use-cases/storing-comments/) utlines the basic patterns for storing user-submitted comments in a content management system (CMS).
* [Use Case: Storing Log Data](http://docs.mongodb.org/ecosystem/use-cases/storing-log-data/) outlines the basic patterns and principles for using MongoDB as a persistent storage engine for log data from servers and other machine data
* [Use Case: Pre-Aggregated Reports](http://docs.mongodb.org/ecosystem/use-cases/pre-aggregated-reports/) outlines the basic patterns and principles for using MongoDB as an engine for collecting and processing events in real time for use in generating up to the minute or second reports

### Some basic facts

* Schema-less
* Collections of Documents
* A single JavaScript call will retrieve a document and all of its nested content; getting into nested content involves further operations
* JSON output (data stored as BSON)
* Object IDs: always 12 bytes, composed of a timestamp, client machine ID, client process ID, and a 3-byte incremented counter; this autonumbering scheme makes that each process on every machine can handle its own ID generation without colliding with other _mongod_ instances (source: «7 databases in 7 weeks», p.138)
* Javascript for queries and manipulation
* No server-side joins
* Map-reduce queries

