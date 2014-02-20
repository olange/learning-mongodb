# Session 3 · 20.02.2014 · Build an Application Series

Part Two · Interacting with the database

## Further reading

* [Use Case: Storing Log Data](http://docs.mongodb.org/ecosystem/use-cases/storing-log-data/) outlines the basic patterns and principles for using MongoDB as a persistent storage engine for log data from servers and other machine data
* [Use Case: Pre-Aggregated Reports](http://docs.mongodb.org/ecosystem/use-cases/pre-aggregated-reports/) outlines the basic patterns and principles for using MongoDB as an engine for collecting and processing events in real time for use in generating up to the minute or second reports.

## Live Chat

Eoin Brazil: Hi All, don't forget that if you have specific questions after this talk or on other topics you can post them to our Google Group - https://groups.google.com/forum/#!topic/mongodb-user

Eoin Brazil: For anyone who is interested these slides and the related video will be available on our website under the event page. Our last session, 2, can be found at http://www.mongodb.com/presentations/webinar-build-application-series-session-2-getting-started

Adam Comerford: @Andrew Mori - the mongodb-user group is where to go for the C driver (and Jira of course): https://github.com/mongodb/mongo-c-driver#support--feedback

Jon Rangel: @andrewkentish asked about storing data to track changes over time.  There are some good examples on schema design for storing time series data in MongoDB here: http://docs.mongodb.org/ecosystem/use-cases/pre-aggregated-reports/.  Also, see this blog post: http://blog.mongodb.org/post/65517193370/schema-design-for-time-series-data-in-mongodb

Norberto Leite: Andy asked: Is there a $notexists command?
Yes there is http://docs.mongodb.org/manual/reference/operator/query/ne/
with this you can check the differences between documents that have certain fields from others that don't

Sam Weaver: @Byron Tie - yes that's how projections work. Anything that you don't specify in the project is assumed as 0, except for _id. That is the only thing that requires an explicit set to 0 or it will come back

Henrik Ingo: Continuing to Andy's question: You may also want to combine $not and $exists to get what you're asking: http://docs.mongodb.org/manual/reference/operator/query/not/#op._S_not

Henrik Ingo: Paras asked if there is an IN operator. Yes, it's called $in http://docs.mongodb.org/manual/reference/operator/query/in/

Matthew Bates: Andrew asked about how to specify which document is updated. The first parameter to the update method is a query; this can be a query for an exact match (ie with _id) or any other query using the query selectors. More info at http://docs.mongodb.org/manual/reference/method/db.collection.update/.

Henrik Ingo: Paras asks if using IN has any performance overhead in a sharded cluster (like it has in Cassandra, apparently)? Answer: it's no different from any other query. Depending on the elements you list in the $in array, the query will be sent to a single shard, or all of them, as needed. Each shard will then perform the query in parallel. (So in many cases, a sharded cluster will be faster than a single server.)

Jon Rangel: @Antonis asked how the content in this webinar series compares to the MongoDB University online education courses:  The topics covered here are broadly similar to those covered in the M101 course, but the online courses additionally have hands-on exercises and go deeper in a number of areas.  The online M101 course also comes in 3 flavours: M101J for Java developers, M101P for Python and M101JS for Node.js devs

Norberto Leite: Zafrul asked: so how are the comments 4,5,6 AND 7,8,9 associated with original document ? will they go into different buckets ?
When you perform a $push on an array what happens is that they are appended to the beggining of the array structure. They are still part of the original document:http://docs.mongodb.org/manual/reference/operator/update/push/

Eoin Brazil: Hi @Antonis, in addition to the courses on MongoDB University mentioned by Jon we have a DBA specific course M102 and a follow M202 for Advanced deployment and operations. All of these courses are free.

Norberto Leite: Sergio asked: what means single atomic opeation??
Atomic operation means that every instruction received and executed by the mongodb (mongod) server will be completed. This means that a document cannot partially changed in what an operation is concerned. If update 10 fields, all 10 fields will be changed. If insert a document the full document is inserted. http://docs.mongodb.org/manual/faq/fundamentals/#does-mongodb-support-acid-transactions

Jon Rangel: @Rotem Gabay asked: How to decrement counters in an update operation? Answer: Use the $inc update operator with a negative value.  For example: $inc : { "daily.comments" : -1 }

Henrik Ingo: Byron asks if write concern can be used to insert 2 documents as an atomic transaction? The answer is no. In MongoDB an insert/update/delete is atomic separately for each document. Write concerns do not change this at all. Write concerns simply affect at which point the connector returns the call to the application: after the write is applied, after it is flushed to disk, after it is replicated, and so on. But it doesn't change the atomicity of each write operation.

Adam Comerford: Rotem Gabay asked: in case i dont have a jornal file when will the daa be flushed to disk? in case i dont have a jornal file when will the daa be flushed to disk? Answer: Without a journal file the flush to disk is every 60 seconds in the background by default (fsync).  Running without a journal is *not recommended* in any scenario where you care about your data.

Eoin Brazil: Hi All, just a reminder that the hashtag for this series of webinars is #MongoDBBasics

Henrik Ingo: Paras asks if there are any issues wrt MongoDB writes using EBS on EC2? Answer: No, except that the standard EBS has really poor performance. On the other hand the Provisioned IOPS and High IO options on EC2 have great performance and Amazon is a very popular platform to deploy MongoDB on.

Norberto Leite: Clayton Piscopo asked: Will practical side to Replica Sets covered on these webinars?
Yes, stay tunned!

Eoin Brazil: Hi All as @Rotem asked, the first webinar is at http://www.mongodb.com/webinar/intro_mongodb_jan14 and the second webinar is at http://www.mongodb.com/presentations/webinar-build-application-series-session-2-getting-started

Matthew Bates: Daniel Maxerov asks where he can read more about bucketing and overflowing comments: best place to start is at the MongoDB docs, with an article on patterns for storing comments. http://docs.mongodb.org/ecosystem/use-cases/storing-comments/. Talks about  schema design, indexing and sharding considerations. 

Adam Comerford: Rotem Gabay asks: what is writte to the jornal? all of the data ? Answer: it actually is flushing write-ahead redo logs, and has a concept of group commits, so yes (sort of), but it's more complicated than that.  You can find out more here: http://docs.mongodb.org/manual/core/journaling/ and here: http://www.mongodb.com/presentations/storage-engine-internals

Daniel Roberts: Thanks for your time guys… See you next time…!

Eoin Brazil: The next webinar, 3rd in the series, will be on the 6th of March covering indexing including geo spatial and full text search. The 4th webinar in the series, on March 20th will focus on aggregration and reporting. If you have registered you will receive a follow up email with the details as a reminder. Hope to see you all on the 6th of March.

Daniel Roberts: Please ping us via #MongoDBBasics

Henrik Ingo: Paras complains that PIOPS EBS costs more. This is true. But it's usually worth it, for example you can often have less RAM when the disk is faster. Anyway, you can also build a RAID of the standard EBS disks to make them faster. Also some people use the ephemeral disks, relying on replication for data durability. Or to be safer you could have a few servers using ephemeral disks and one member of the replica set using an EBS disk (and allow it to be slow).

Adam Comerford: Tony Farrell asks: crazy question...   we need really fast performance...  IT is talking about a SSD...  can the  journal file be on the SSD drive, while the data file(s) are on a standard platter drive? Answer: Usually you want it the other way around.  The access pattern of the data is key - SSD do really well for random access time (no seeking) so for the standard MongoDB data access, they perform really well.  The journal is more of a standard sequential access pattern and so sees less benefit from SSD (though it is still better than spinning disk) and fits a spinning disk better.

Jon Rangel: Anybody interested in deploying MongoDB on Amazon EC2 should also check out this page in the docs for additional deployment tips: http://docs.mongodb.org/ecosystem/platforms/amazon-ec2/

Norberto Leite: Lasse asked: What do you think about a mongoDB hosting service like MongoLab? Is it ok to use for production?
MongoLab has a particular good integration with Windows Azure so if you are thinking on deploying on Azure that might be the best option if you don't want to manage your MongoDB cluster yourself. If you like a complete overview of our cloud partenrs have a look into this: http://www.mongodb.com/partners/cloud

Owen Hughes: Thanks everyone, we are closing down the genius bar. Please ask questions or comment on twitter using #MongoDBBasics

Eoin Brazil: Hi All, If you want to ask deeper questions than twitter allows, you can post to our Google Group https://groups.google.com/forum/#!forum/mongodb-user and we can continue the conversation there until the next webinar.

Adam Comerford: Lasse Soberg asks: Ok, I'm currently on AWS and I see that they support almost all regions. How is their hosting on AWS compared to Azure?  Answer: we've definitely seen more usage and there is more collateral (guides, whitepapers) for AWS, but Azure and other platforms are supported.  Best thing to do is test for your use case and see how it performs.

Chairperson: Thanks to everyone for attending.  This Session will be closing in 2 minutes.  Please ask questions or comment on twitter using #MongoDBBasics
