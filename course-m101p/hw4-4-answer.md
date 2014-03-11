# Homework 4.4

Analyze a profile log taken from a mongoDB instance [Description complète](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_4_Performance/52cf29bae2d423570a05b92d/)

## Pièces jointes

* [hw4-4-sysprofile.acfbb9617420.json](hw4-4-sysprofile.acfbb9617420.json) jeu de données mis à dispo par Mongo

## Problème

In this problem you will analyze a profile log taken from a mongoDB instance. Query the profile data, looking for all queries to the `students` collection in the database `school2`, sorted in order of decreasing latency. What is the latency of the longest running operation to the collection, in milliseconds?

## Résolution

    $ mongo
    > db.profile.find({ op:"query", ns:/school2.students/})
                .sort({ millis: -1}).limit( 1)
    { "_id" : ObjectId("531604231f113c79eae77957"), "ts" : ISODate("2012-11-20T20:09:49.862Z"), "op" : "query", "ns" : "school2.students", "query" : { "student_id" : 80 }, "ntoreturn" : 0, "ntoskip" : 0, "nscanned" : 10000000, "keyUpdates" : 0, "numYield" : 5, "lockStats" : { "timeLockedMicros" : { "r" : 19776550, "w" : 0 }, "timeAcquiringMicros" : { "r" : 4134067, "w" : 5 } }, "nreturned" : 10, "responseLength" : 2350, "millis" : 15820, "client" : "127.0.0.1", "user" : "" }

## Réponse

    15820

## Préparation

    (venv) course-m101p $ mongoimport -d m101 -c profile < hw4-4-sysprofile.acfbb9617420.json
    connected to: 127.0.0.1
    Tue Mar  4 17:49:39.868 check 9 1515
    Tue Mar  4 17:49:39.868 imported 1515 objects
