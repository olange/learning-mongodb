# M101P · Week 3 · Schema Design

Notes and homework related to [Week 3: Schema Design](https://education.10gen.com/courses/10gen/M101P/2014_February/courseware/Week_3_Schema_Design/). 2 hours for the videos, 2 hours for the homework.

## Homework

* [Homework 3.1](hw3-1-answer.md) Write a [program](hw3-1-remove.py) to remove the lowest homework score for each student
* [Homework 3.2](hw3-2-answer.md) Adapt [blogPostDAO.py](hw3-2-blogPostDAO.py) to make your blog accept posts
* [Homework 3.3](hw3-3-answer.md) Adapt [blogPostDAO.py](hw3-3-blogPostDAO.py) to make your blog accept comments

## Recap

### General considerations

* Application-Driven Schema -- matching the data access patterns of the application (very different from normalization in relational databases, which try to avoid bias toward any particular data access pattern)
* Rich Documents
* Pre Join / Embed Data -- always try to embed the data, which allows to keep the data consistent in some way (the foreign keys will be right)
* No Mongo Joins -- if you have to read ids and seek in another collection, you're probably doing it the relational way, not the Mongo way
* No Constraints
* Atomic Operations within a single document -- not ACID: no transactions over multiple documents or tables (can be alleviated by restructuring data, or by implementing the transaction in software, such as when transfering money between two distinct banking systems); eventual inconsistency of state of data between multiple clients (which can be tolerated in most cases)
* No declared schema

### Modeling relationships

* **1:1 relationship**, such as Employee/Resume, Building/Floor plan, Patient/Medical history -- considerations for embedding or keeping in separate collections: 1. depending on frequency of access (if mostly updating Resume but leaving Employee as is, maybe better to have separate collections); 2. size of items (documents must be <16 MB) and working set size in memory (if embedded, both documents are loaded into memory when pulled); 3. atomicity of data (embed to allow atomic update of both documents at once)
* **1:many relationships**, such as City/Person -- it is recommended to use **document linking** (and multiple collection) whenever the *many is large* (true one to many), to avoid duplication and enforce consistency: People `{ name: "Andrew", city: "NYC" }`, City `{ _id: "NYC", area: … }`; whenever the *many is actually few* (one to few), such as Blog Post/Comments, it's probably better to **embed** documents: `{ title: "Blog title", comments: [ … ]}`
* **Many:many relationships**, such as Books/Authors, Students/Teachers: Books to Authors is probably Few to Few (each book has a small number of authors, each author has a few books); recommend to model as two entities, with references to the _id in arrays; embed for performance reason, if needed, but at the risk of duplicating data; the same applies to Students/Teachers: model as separate entities (Students `{ _id: 1, name: "Andrew", teachers: [1,2,3,4,5]}`, Teachers `{ _id: 2, name: "Mark Horowitz"})`, with the additional reason that, you'll probably start adding teachers in the system, and then students
* Multikey Indexes, for each value in an array of a field: how to find all students having given teachers? `db.students.ensureIndex({"teachers":1})`, `db.students.find({"teachers": {"$all": [1,3]}})`; `find(…).explain()` proves that Mongo has indeed used an index; multikey indexes allow to query efficiently on embedded and linked documents
* **Benefits of embedding**: improve read performance -- disks have high latency (it takes 1 ms to get to the first byte) and high bandwidth (the next bytes come very fast), so it is better to have data co-located; on the other side, writes might need to move the document around, if the document size expands 
* **Representing trees** such as Products/Categories, where Categories is a hierarchy (Outdoors > Winter > Snow): leverage the fact that Mongo can store arrays: Products `{ name: "Leaf Blower", category: 7 }`, Categories `{ _id :7, name: "Snow", ancestors: [ 3, 5] }`; to find all descendants of category 7 Snow: `db.categories.find({ ancestors: 7})`

### When to denormalize?

*  In the relational world, we're normalizing to avoid _modification anomalies_
* As long as we don't duplicate data, we do not open to modification anomalies
* In 1:1 relationships, it is OK to embed the data, as we do not duplicate data
* In 1:many, when embedding from the many to the one, we do not duplicate data; when embedding from the one to the many, use document linking to avoid the duplication of data; however, it would make sense to embed for a performance reason, especially if the data is rarely changing or being updated
* In Many:Many, link documents to avoid modification anomalies thru arrays of object ids.

If you're duplicating data, it's up to you, the application programmer, to keep the data up to date.

### Handling large files (BLOBs)

* GRIDFS -- stores large files (>16MB) in chunks and metadata in a separate collection
* Storing a file: `grid = gridfs.Gridfs( db, "videos"); f = open( "video.mp4", "r"); _id = grid.put( f); f.close(); db.videos_meta.insert({ "grid_id": _id, "filename": "video.mp4"})`
* Retrieving: `db.videos.files.find({"_id": _id})`; the data itself is in `db.videos.chunks`
