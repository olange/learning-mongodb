# Session 2 · 06.02.2014 · Build an Application Series

Part One · Getting started · Schema design and application architecture

## Summary

* Flexible schema documents with ability to embed rich and complex data structures for performance
* Schema is designed around data access patterns – and not data storage
* Referencing for more flexibility
* Develop schema with scale out in mind; shard key consideration is important.

## Further reading

* [myCMS Skeleton source code](http://www.github.com/mattbates/mycms_mongodb)
* [Data Models](http://docs.mongodb.org/manual/data-modeling)
* [Use Case: Metadata and Asset Management](http://docs.mongodb.org/ecosystem/use-cases/metadata-and-asset-management/) describes the design and pattern of a content management system using MongoDB modeled on the popular Drupal CMS
* [Use Case: Storing comments](http://docs.mongodb.org/ecosystem/use-cases/storing-comments/) utlines the basic patterns for storing user-submitted comments in a content management system (CMS).

## Getting ready with the MyCMS Skeleton Code

	$ git clone http://www.github.com/mattbates/mycms_mongodb
	$ cd mycms_mongodb
	$ virtualenv venv
	$ source venv/bin/activate
	$ pip install -r requirements.txt

	$ mkdir -p data/db
	$ mongod --dbpath=data/db --fork --logpath=mongod.log

	$ python web.py
	$ deactivate

## Live Chat

[…]

Jon Rangel: @Raju, yes we have an officially supported Scala driver

John Page: @Raju - MongoDB does support Scala and this webinar will not mention mongoviewer, no.

alain helaili: @Chen asked if MongoDB could guarantee writes.  Yes, MongoDB has several levels of write concerns so one can ensure that data has been written to one or several servers

Nick Geoghegan: Nathan: No

Arthur Viegers: @sumit: MongoDB is an operational database, hadoop is not. Hadoop is for offline crunching of data.

Henrik Ingo: @sumit asks about difference between MongoDB and Hadoop. These are two different databases / data storage products. Hadoop is typically used only for quite heavy batch analytics. MongoDB is more like a traditional database, can be used both for app development and analytical data storage.

Daniel Roberts: Is the sound better than last week?

Nick Geoghegan: Paras: It depends on your usecase. An m1.medium is good, as it guarentees CPU, RAM and networking

Henrik Ingo: @Jean-Babtiste, yes, the recording, slides and code examples will be made available after the webinar.

John Page: @James asks about file locking and writes - MongoDB uses lock to ensure multiple threads do not corrupt data but these locks are held for a very short time and writes can be scaled fairly easily to hundreds of thousands per second.

Nick Geoghegan: Paras: There are also MongoDB AMIs available in the AWS marketplace

Eoin Brazil: Hi Leon Liang - if you want to learn about schema's you can watch the first webinar in this series at - http://www.mongodb.com/webinar/intro_mongodb_jan14

Daniel Roberts: Code is at git.io/BldUqA

Nick Geoghegan: William: No, YOU have the best surname ;-)

Tugdual Grall: @sumit : I invite you to look at this Webinar about Hadoop and MongoDB: http://www.mongodb.com/webinar/mongodb-hadoop-jan2014

Sharon Elkayam: @Shlomo: The previous webinar slides and recordings can be found here: http://pages.mongodb.com/017HGS5930003q800E8aY00 and http://pages.mongodb.com/017HGS5930003q900E8aY00



Arthur Viegers: @ofri: only actions on documents are atomic in MongoDB. You cannot do atomic actions affecting more than one document.

Nick Geoghegan: Paras: For production, 3 nodes in a replicaset is best. It gives you high availablity and redundency. 

Tugdual Grall: @Antonio, yes you have some tools to integrate with reporting tools such as Pentaho , Jasper Report, for the forms today people are using many Web framework depending of your programming language

Owen Hughes: The webinars will be recorded for playback later. The code will be posted to Github

Henrik Ingo: @ofri asks about transactions or atomicity. The answer is that updates are atomic on a per-document granularity. So for example updating 2 fields in the same document is atomic. This turns out to be surprisingly useful. However, updating multiple documents is not possible in a transactional, atomic manner. See  http://docs.mongodb.org/manual/tutorial/perform-two-phase-commits/ for more info

alain helaili: re there tools for windows forms and reporting?

Nick Geoghegan: Dejan: It is not recommended as openVZ does interesting things with memory management. 

alain helaili: @Antonio asked if there were tools for windows forms and reporting : there are a bunch of frameworks on the market and some reporting tools such as Pentaho and Jaspersoft provide support for MongoDB

Arthur Viegers: @ofri: Yes, the only way to do this is to handle it at the application level.

Tugdual Grall: @Roland, both are good, it really depends of your application logic.

John Page:  Lets say I had 5,000 writes to perform for a single database, but different collections. Is this a bad idea? Would it take a long time?

Henrik Ingo: @Bojan asks about Lucene indexing. To be precise, MongoDB 2.4 introduced full text indexes. This is a MongoDB feature implemented by ourselves, it is not based on Lucene. In other words, you can use MongoDB full text search, or use a separate lucene server if you specifically want lucene.

Eoin Brazil: Hi @Chen Roth - you can look at our case studies for ecommerce at http://www.mongodb.com/industries/retail or contact us (https://www.mongodb.com/contact) and we'll have a sales rep talk to you directly

Ger Hartnett: @roland Reusing objectid will encapsulate timestamps and save you having to make sure the id is unique.

John Page: @Sergey - it's technically possible to implement distributed transactions but it's not a focus for us as for most use cases - if you understand how to use the document model you don't need them. It's like asking when Node.JS is going to implement threads.

alain helaili: @Shilpen asked about monitoring tools : There are a bunch of monitoring tools such has mongostats and MMS. 

Sharon Elkayam: @Borat - that depends on the requirements you have from text search in your application. MongoDB built-in text search covers stemming and tokenization for 14 languages at the moment, including support within aggregation framework (2.6). more details can be found on our official docs

Nick Geoghegan: Levi: Yes, it wll be available later. 

Henrik Ingo: @Samuel asks if the sample app is available for Java? We use Python for this webinar series, as it should be an easy language for everyone to follow. However, we plan to do a similar series with Java and JavaScript later.

Eoin Brazil: Hi @Sohail Iqbal, do you want to put a post in Google Group with your product example and we can discuss it in more detail there - https://groups.google.com/forum/#!overview

Olivier Lange: Clojure is missing from the survey; it is my language of choice

Nick Geoghegan: Shilpen: On disk, or in transit? In transit, yes - using SSL.

Tugdual Grall: @Martin at the end the native drive is used. Mongoose is just an ODM (Object Document Model) so it depends really of your application and how you want to develop. What I saw from npm stat is 50% of the developers seam to use the node native driver alone other with a top layer such mongoose

Ger Hartnett: @Sergey if you really want to distribute transactions across documents you can use this design pattern http://docs.mongodb.org/manual/tutorial/perform-two-phase-commits/

Arthur Viegers: @Shilpen: MongoDB does not encrypt data at rest. SSL on all members in a replica set is supported.

Eoin Brazil: Hi @joe connolly, can you provide a little more detail on your serialiser question with the console/log output in Google Group - https://groups.google.com/forum/#!overview

Tugdual Grall: @Shilpen : you can get some stats from your database using mongostat, and explain; take a look to http://docs.mongodb.org/manual/reference/program/mongostat/

Henrik Ingo: @Samuel asks if there is sample code in Java available on Github? No, not related to this webinar specifically. To get started with MongoDB in Java, have a look at http://docs.mongodb.org/ecosystem/tutorial/getting-started-with-java-driver/

Ger Hartnett: @olivier There are a number of clojure MongoDB drivers

Arthur Viegers: @Daniel: You can reuse your DB object (it is what I do by default). In your connection to the DB configure it to auto-reconnect in case the DB connection gets lost.

alain helaili: @Maor asked if there are ORM for Mongo : yes, there are multiple choices here, but you'll find you don't need it that much 

Massimo Brignoli: @Andreas is asking about concurrency: MongoDB has a database level locking, so at the end you will have the last value

Tugdual Grall: @Maor: yes you habe Morphia ( https://code.google.com/p/morphia/ ) or Hibernate OGM (https://docs.jboss.org/hibernate/ogm/4.0/reference/en-US/html_single/#ogm-mongodb ) but sometimes it is also good to stay with the native driver just to keep the benefits of "dynamic approach"

alain helaili: @Willial asked : Adding an image to a document is only possible when the image is not bigger than 16MB? Yes, GridFS in MongoDB does that.

Daniel Roberts: @Sumit - Yes… use Spring Data for MongoDB…  We have customers in production using it.

Tugdual Grall: @William you if you need to store "files" you can use GriFS that allow you to store files in the database http://docs.mongodb.org/manual/core/gridfs/  

Daniel Roberts: np

John Page: @Tibor asks when to use one or many collections - generally each type of record shoudl be in one collection althought they don't have to be identical take a new collection when there is no reason to put them in the same one.

Arthur Viegers: @Santi: You can use GridFS to store pictures in MongoDB

Marc Schwering: @Maor, yes there are ODM (Object Data Mapper) for some Languages like Morphia (https://code.google.com/p/morphia/) or Spring http://projects.spring.io/spring-data-mongodb/  and there is hibernate support.

Nick Geoghegan: William: Lots! 24000

Nick Geoghegan: William Geoghegan: That's the default, mind you. It can be increased fairly easily enough

Tugdual Grall: @Andreas Gridfs create chunks and store that in a special collections http://docs.mongodb.org/manual/core/gridfs/

Nick Geoghegan: William  Geoghegan: Yeah. Be a bit of a nightmare to admin, though. It'd depend on your usecase 

Charlie Page: @Carlos you can't change the max 16meg size without modifing the source code

Henrik Ingo: @Thomas asks why there is a 16 MB limit for document size? It is a somewhat arbitrary decision. 16 MB is quite a lot for most cases, for example it is more than the longest book ever written. You can also store larger objects in a MongoDB cluster using the GridFS API. This can take a large file, which contents is transparently split and stored into multiple records, each smaller than 16 MB.

Henrik Ingo: A lot of questions about GridFS. See http://docs.mongodb.org/manual/core/gridfs/ for getting started / quick overview.

Charlie Page: @Andy a schema is what your program expects to find in the database essentially.  The objects are singular but a find can return one or many of them

John Page: take a new collection when there is no reason to put them in the same one.

Nick Geoghegan: Schmuel: On disk, there will be fragmentation. This space will try to be used again, by the storage algorithm

John Page: @Miguel asked is _id is a naming convention, yes the Primary Key field (identifier) must always be called _id its the only field you MUST have

Ger Hartnett: @Jean-Baptiste The document limit does not apply to blobs stored in GridFS

Henrik Ingo: @Jean-Babtiste it is possible to store objects or files larger than 16 MB using the GridFS API. See my link earlier in this chat.

Tugdual Grall: @Andreas if you do not use GridFS, you have to "explode" the document yourself

Jon Rangel: @Tibor: there is no limit on the number of fields in a document, only on the maximum size of the document (16MB)

Henrik Ingo: @Rajesh asks, when you delete comments from the array, would your document still be contiguous in memory? The answer is yes. Essentially the document is "rewritten" in place.

Sharon Elkayam: @Rui Pedro Lima - yes, it is supported

Eoin Brazil: Hi @Amisha Patel - there will be a DBA course in Feb - https://education.mongodb.com/courses/10gen/M102/2014_February/about and an advanced ops course in March, https://education.mongodb.com/courses/10gen/M202/2014_April/about

Nick Geoghegan: Tibor: 16MB is a lot of data - imagine all the works of shakespere and Arthur Conan Doyle together...you would still have PLENTY of room free

Arthur Viegers: @Francois-Xavier: GridFS stores your data over to collections: one to store the data and the other to store the meta data.

John Page: @Miguel asked is _id is a naming convention, yes the Primary Key field (identifier) must always be called _id its the only field you MUST have

Eoin Brazil: Hi @Fulvio Di Domizio, we provide GridFS to act as a file storage layer for larger documents than 16MB

Tugdual Grall: @Mohamed Yes you have ETL connectors for exampel for Informatica, Talend see our partners page: http://www.mongodb.com/partners/software

Henrik Ingo: @Mohamed asks if it is possible to pull data from MongoDB using conventional ETL tools. A few ETL tools already support MongoDB (really well). See http://www.mongodb.com/partners/software

alain helaili: @Maor asked if updating an existing document without reading the document completly into memory was possible. Yes, you do not need to read the document to update it

Ger Hartnett: @Aleksandr there had to be some limit and 16MB was ensures a single document cannot use excessive amount of RAM or, during transmission, excessive amount of bandwidth

Tugdual Grall: @Andreas, you will get an exception. But remember 16Mb is JSON is HUGE!

Massimo Brignoli: @Ritesh: check GridFS in our manual page: http://docs.mongodb.org/manual/core/gridfs/

Nick Geoghegan: Dejan: It takes up RAM, which can be used for data instead of names

Eoin Brazil: Hi @Dimtry Kiselev, we don't support embedded platforms at this point in time, our supported platforms can be see at http://www.mongodb.org/downloads

Charlie Page: @Colm collections should be used to divide your data up logically, however you can also use it break up data for other reasons.  There is complete data modeling information here: http://docs.mongodb.org/manual/data-modeling/

Charlie Page: @Maor you have to read it all into memory

Nick Geoghegan: Taaniel: By reusing space. If your document is expected to grow in size, over time, you can use "power of 2 sizes" to limit the fragmentation on disk 

Ger Hartnett: @Maor, yes you can update a document without loading it all into memory first

Jon Rangel: @Bojan Saric asked for confirmation about the most recent data model shown:  this is one article document containing the most recent 10 comments, and one document per comment bucket, each containing up to 100 comments

Sharon Elkayam: @Sean Furth - you can also use capped arrays (introduced in version 2.4)

Charlie Page: @Moar MongoDB loads a document into memory to modify it

John Page: @Maor - that's actually a tricky question so you got two answers - on the server, the whole record will be read from disk into RAM during the update - but you do not need to pull the whole document to your client , update it and push it all back to the server. Hope that clears it up.

Henrik Ingo: @Mykhailo asks if it costs a lot to update the arrays or buckets? The answer is that in MongoDB updates of documents are often "update in place", which is very efficient. But this is not always the case, there are several things that can lead to inefficient updates.

Eoin Brazil: Hi @Vihang Shah, in this example there is no caching layer but you can easily add another cache layer for performance if required

Jon Rangel: @mykhailo tiurin asked about updating the "top 10" array in the article document.  MongoDB provides an easy and efficient way to maintain 'capped' arrays of this nature:  http://blog.mongodb.org/post/58782996153/push-to-sorted-array

John Page: @Jean Baptiste - there is no real reason we took Bottle and Angular for this but we had to choose something, your choice of UI frameworks does not affect how you design Schemas and use MongoDB hopefully.

Olivier Lange: Is there an easy way to measure time taken by a query from the shell? db.coll.find().explain() does not seem to return time.

Eoin Brazil: Hi @sumit kumar & @chris burton - there are details regarding the setup and install of PIP available at - http://www.pip-installer.org/en/latest/

John Page: @Oliver asks how to measure time taken for a query from the shell, use explain() and look in the millis field.

John Page: @Oliver asks how to measure time taken for a query from the shell, use explain() and look in the millis field.

Henrik Ingo: @Shlomo asks if there is a library in C# that converts objects to BSON. In fact the MongoDB C# connector can do exactly that. http://docs.mongodb.org/ecosystem/tutorial/serialize-documents-with-the-csharp-driver/

Arthur Viegers: @Burim: We will do a node.js webinar later in the series.

alain helaili: @Burin asked about a node.js demo : We're working on it. Coming soon.

John Page: @Mykhalio - this app is similar to the one in M101P but not exactly the same

Massimo Brignoli: @Rajender: We will have a java webinar later in the series

alain helaili: @Rui asked about indexing embedded fields : this is totally doable and won't hurt at all. Actually, probably a good idea if you're going to query on that.

Tugdual Grall: @Rajender @Alession : yes we will have a Webinar around Java Development - You can also start looking that the Java Driver tutorial here : http://docs.mongodb.org/ecosystem/tutorial/getting-started-with-java-driver/#getting-started-with-java-driver

Massimo Brignoli: @Gianni: Yes, I'll replicate this webinar series in italian starting the 11th of march

Olivier Lange: oh! I missed the millis field. Thanks. So this works: db.users.find({"user":"mattbates"}).explain() -> { ..., millis: 6, ... }

Eoin Brazil: Hi Jean-Baptiste, this is a longer question can you post the Ember/Python/MongoDB schema layout you envisage and questions at our Google Group https://groups.google.com/forum/#!forum/mongodb-user

Massimo Brignoli: @Gianni: Prego, if someone is close to Milan, can come also to our mongodb user group, next meeting the 18th of march

Arthur Viegers: @Denizhan: You can use your own created unique values for the _id field (even composites are allowed). There are no performance drawbacks. The only requirement is that the value is unique in the collection.

John Page: @Denzian asks what the implications of supplying _id yourself are. It can be faster than using auto generated _id's but you are responsible for generating unique ones also there are performance implications at the high end where constantly incrementing _id's are faster than random unless using shards where you need to understand how to get optimal ones as shard keys.

Laura Czajkowski: To find your nearest MongoDB Meet up haev a look at http://www.mongodb.com/user-groups-mongodb

Massimo Brignoli: @Fulvio @Gianni: check the meetup page: http://www.meetup.com/MongoDB-Milan/ 

Laura Czajkowski: Sign up to the news letter to know when the nearest and newest event is happening http://www.mongodb.com/newsletter

Eoin Brazil: Hi @Mykhailo Tiurin, there are a few good presentations on example schemas - http://www.slideshare.net/friedo/data-modeling-examples and design pitfalls - https://blog.serverdensity.com/mongodb-schema-design-pitfalls/

John Page: @Shlomo asks - do you get the _id on inserts - yes you do

alain helaili: Cam I update an existing document without reading the document completly into memory?

Massimo Brignoli: @Manuel: this is the madrid user group:

Massimo Brignoli: http://www.meetup.com/Madrid-MongoDB-User-Group/

Laura Czajkowski: List of  all user groups can be found - http://www.mongodb.com/user-groups-mongodb

Nick Geoghegan: Nicolas: Yes, they will all be made available after the talk. http://www.mongodb.com/webinar/intro_mongodb_jan14 

Sam Weaver: @Daniel Maxerov: it would be done manually. 

Henrik Ingo: @Simone asks if we can do Java examples next time? Answer is "no", this series will continue in python. But there will be another series later which is in Java. Note that we also have a Java based developer course M101J  on education.mongodb.com.

Nick Geoghegan: William G: So are we!

John Page: @Denzian asks what the implications of supplying _id yourself are. It can be faster than using auto generated _id's but you are responsible for generating unique ones also there are performance implications at the high end where constantly incrementing _id's are faster than random unless using shards where you need to understand how to get optimal ones as shard keys.

John Page: @Jay Ma asks how you can generate a unique sequence value - _id's are generated by a combination of datetime/client ip/process id/ oneup in the client not from the server. If you want to generate your own you can use findAndModify and $inc to create something like a sequence although for performance you would  want to batch requests to it to avoid a server call each time.

Sam Weaver: @jay ma: the _id is generated automatically using a hash of mac address, and timestamp and some other things which makes it unique. You can over-ride it with your own value if you like You can also ensure it has a unique index so no duplicates can exist.

Sam Weaver: @Ritesh Aryal: http://www.php.net/manual/en/class.mongodb.php

Eoin Brazil: Hi @Laurence Curtis, it depends on whether each user is represented by a document or whether a list of user is represented in a single document. A longer question at https://groups.google.com/forum/#!forum/mongodb-user might be better to explain these differences.

John Page: @Maor - Already answered that, yes you cab get back a subset of ids using the project property in the query to choose the fields you want back.

Eoin Brazil: Just a reminder to all the hashtag for this session is #MongoDBBasics if you want to follow up over twitter

Nick Geoghegan: William Geoghegan: I play icecream truck music

Marc Schwering: For PHP i suggest you should take a look into: http://www.php.net/manual/en/mongo.tutorial.php  There are also existing web frameworks using MongoDB and PHP like Lithium: http://li3.me/

Henrik Ingo: @Vivek asked why it is not adviceable to have an unbound array that can grow in size, is it not good practice? From a style point of view it is actually not a problem to do that. The reason we discourage it is that an update that makes the document grow, can be much more expensive. It may cause that the document has to be moved to another physical location, with new space allocated for it, and index pointers updated. Especially if the array field itself is index, that can cause a lot of index updates. Other than performance reasons, there is no problem in growing arrays. Also, you of course need to be mindful of the 16MB limit, but usually you don't come anywhere close to that.

Massimo Brignoli: Agli italiani in ascolto:  il prossimo meetup di MongoDB Milano sara' il 18 marzo presso la sede di Red Hat Italia, in via Gustavo Fara 28 alle ore 19.00
