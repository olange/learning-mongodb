# Session 1 · 30.01.2014 · Getting started

Back to Basics · Introduction

## Summary

* Document Model
  * Simplifiy development
  * Simplify scale out
  * Improve performance
* MongoDB
  * Rich general purpose database
  * Built in high availability and failover
  * Build in scale out

## Further reading

* [Analyze Performance of Database Operations](http://docs.mongodb.org/manual/tutorial/manage-the-database-profiler/) enable with `db.setProfilingLevel(2)` and query with `db.system.profile.find( { millis : { $gt : 5 } } ).pretty()` for instance; `show profile` displays the five most recent events that took more than 1ms
* [Measuring time and analyzing a query: explain()](http://docs.mongodb.org/manual/reference/method/cursor.explain/) `db.collection.find().explain().millis` gives the time taken by a given query
* [Ways to implement data versioning in MongoDB](http://stackoverflow.com/questions/4185105/ways-to-implement-data-versioning-in-mongodb) StackOverflow
* [Atomic Counters using MongoDB’s findAndModify with PHP](http://chemicaloliver.net/programming/atomic-counters-using-mongodbs-findandmodify-with-php/)
* [How to apply automatic versioning to a C# class](http://stackoverflow.com/questions/20351698/how-to-apply-automatic-versioning-to-a-c-sharp-class)

## Live Chat

(pas sauvegardé cette fois-là)