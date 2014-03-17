# M101P · Week 5 · Aggregation Framework

Notes and homework related to [Week 5: Aggregation Framework](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_5_Aggregation_Framework/).
 
## Homework

* [Homework 5.1](hw5-1-answer.md)
* [Homework 5.2](hw5-2-answer.md)
* [Homework 5.3](hw5-3-answer.md)
* [Homework 5.4](hw5-4-answer.md)

## Additional resources

* [Aggregation reference](http://docs.mongodb.org/manual/reference/aggregation/) (MongoDB Manual)

## Recap

* Simple example: `db.products.aggregate([ { $group: { _id: "$manufacturer", num_products: { $sum: 1}}}])` returns a document with fields `_id` and `num_products`, containing a product count per manufacturer
* Compound grouping: `db.products.aggregate([ { $group: { _id: { "manufacturer": "$manufacturer", "category": "$category" }, num_products: { $sum: 1}}}])` is similar to `SELECT manufacturer, category, COUNT(*) FROM products GROUP BY manufacturer, category`
* By the way, documents can be used for `_id` in general: `db.foo.insert({ _id: { name: "andrew", class: "m101"}, hometown: "NY"}` is perfectly valid

### Aggregation pipeline

* Documents of a collection are piped thru an _aggregation pipeline_, which is a queue in FIFO-order of _aggregation operations_ (or _aggregation stages_), that is going to transform the collection
* … expressed by `db.products.aggregate( ‹pipeline›)` in the Mongo shell, where _‹pipeline›_ is an _ordered array_ of _aggregation operations_
* … each operation can appear more than once in the pipeline, at different _stages_
* Sample pipeline: _collection_ → `$project` → `$match` → `$group` → `$sort` → _result_
* `$project` operation -- select, reshape (1:1)
* `$match` operation -- filters (N:1 / reducing effect)
* `$group` operation -- aggregation (N:1 / reducing effect)
* `$project` operation -- sorting (1:1)
* `$skip` operation -- skip documents (N:1 / reducing effect)
* `$limit` operation -- limit number of documents (N:1 / reducing effect)
* `$unwind` operation -- unjoins data of arrays or subdocuments (1:N / augmenting effect), normalizing the data to ease aggregation; for instance, when _unwinding_ its field `tags: ['sports', 'outdoors', 'summer']`, a blog post would be exploded into three documents

### Grouping operation (N:1) · Aggregation expressions

* _Aggregation expressions_ in the **`$group`** stage: `$sum` (sums up the key value with `{$sum: "$price"}`, or sums up the given value to count `'$sum': 1`), `$avg` (average, for instance `{$avg: "$price"}`), `$min` and `$max` (find the minimum and maximum values of the key), `$push` and `$addToSet` (build arrays, the last adding uniquely each key), `$first` and `$last` (both requiring to sort, otherwise the returned keys are arbitrary)
* Sum operation `$sum`: `db.zips.aggregate([{ "$group": { _id: "$state", population: { $sum: "$pop" }}}])`
* Average operation `$avg`: `db.products.aggregate([{ $group: { _id: { category: "$category"}, avg_price: { $avg: "$price" }}}])`
* Building arrays with `$addToSet`: `db.products.aggregate([{ $group: { _id: { maker: "$manufacturer"}, categories: { $addToSet: "$category" }}}])` will build a new set of documents grouped by manufacturer, looking thru the array to see if the category is already there, adding it if it was not; quiz answer: `db.zips.aggregate([{ $group: { _id: "$city", postal_codes: { $addToSet: "$_id" }}}, { $limit: 5}])`; note that the `"$_id"` expression refers to the `_id` in the _source documents_ of the pipeline stage
* Building arrays with `$push`: similar to `$addToSet`, but does not guarantee that it adds each item only once; for instance `db.products.aggregate([{ $group: { _id: { maker: "$manufacturer"}, categories: { $push: "$category" }}}])` would again build a set of new documents grouped by manufacturer, where the categories might appear more than once; quiz: `$push` is obviously identical to `$addToSet` if its expression contains unique values, although the order of documents might be different
* Picking the maximum and minimum value with the `$max` and `$min` operations: `db.products.aggregate([{ $group: { _id: { maker: "$manufacturer"}, max_price: { $max: "$price"}}}])` will find the maximum price of the products of a manufacturer
* However, getting the product matching that maximum price can't be done within this grouping stage alone, additional `$sort` and `$limit` stages would be needed
* Quiz answer: `db.zips.aggregate([{ $group: { "_id": "$state", pop: { $max: "$pop"}}}])`

### Double grouping stages

* To figure out the average class grade in each class, we need to average all the students' grades within the class, and after that first stage, average those grades (aka scores) in a second stage: `db.grades.aggregate([{ "$group":{ _id: { class_id: "$class_id", student_id: "$student_id"}, average:{ "$avg": "$score"}}}, { "$group":{ _id: "$_id.class_id", average:{ "$avg": "$average"}}}])`
* Quiz answer: `db.fun.aggregate([{ $group:{ _id:{ a: "$a", b: "$b"}, c:{ $max: "$c"}}}, { $group:{ _id: "$_id.a", c:{ $min: "$c"}}}])` returns documents `{ _id: 0, c: 52}` and `{ _id: 1, c: 22}`

### Projection operation (1:1)

* Allows to reshape the documents coming thru: remove keys, add new keys, reshape keys, use simple functions on keys, such as `$toUpper`, `$toLower`, `$add` or `$multiply`
* For instance `db.zips.aggregate([{ $project:{ _id: 0, city:{ $toLower: "$city"}, pop:1, state:1, zip: "$_id"}}])` will suppress the `_id` field (`0` means drop it) and replace it with `zip`, including the fields `pop` and `state` as they are (`1` means just include it), plus `city` lowercased (more complex expressions are evaluated)
* Quiz answer: see the example above

### Matching operation (N:1)

* Matching operation `$match`: performs a filter (on the documents as they pass thru the pipe) and has a reducing effect (N:1, or 1:1 if all documents are matched)
* For instance `db.zips.aggregate([{ $match: { state: "NY"}}])`
* Matching and grouping: `db.zips.aggregate([{ $match:{ state:"NY"} }, { $group:{ _id: "$city", population:{ $sum:"$pop"}, zip_codes:{ $addToSet: "$_id" }}}])`
* Matching, grouping and projecting: `db.zips.aggregate([{ $match:{ state:"NY"}}, { $group:{ _id: "$city", population:{ $sum:"$pop"}, zip_codes:{ $addToSet: "$_id"}}}, { $project:{ _id: 0, city: "$_id", population: 1, zip_codes: 1 }}])`
* Quiz answer: `db.zips.aggregate([{ $match: { pop: { $gt: 100000}}}])`

### Sorting operation (1:1)

* Sorting operation `$sort`: before or after grouping stage; beware memory usage! the aggreation framework handles everything in memory
* If the sort is _after_ the grouping stage, the operation won't be able to use an index
* Sort can be used multiple times
* Sorting _before_ grouping is often very useful when aggregating
* For instance `db.zips.aggregate([ …, { $sort: { population: -1 }}])`
* … within a complete pipeline: `db.zips.aggregate([{ $match:{ state:"NY" }}, { $group:{ _id: "$city", population:{ $sum:"$pop" }}}, { $project:{ _id: 0, city: "$_id", population: 1 }}, { $sort:{ population: -1 }}])`
* Quiz answer: `db.zips.aggregate([{ $sort: { state: 1, city: 1}}])`

### Skipping and limiting operations (N:1)

* Skip forward in the document set with `$skip` and limiting the resultset with `$limit`
* The _order_ they are specified **does matter** (to the contrary of `find`); generally you first _skip_, then _limit_
* Skipping doesn't make a lot of sense unless you sort, so you first sort, then skip and/or limit
* For instance `db.zips.aggregate([ … { $sort: { population: -1 }}, { $skip: 10}, { $limit: 5}])`
* … within a complete example: `db.zips.aggregate([{ $match: { state: "NY"}}, { $group:{ _id: "$city", population:{ $sum: "$pop"}}}, { $project:{ _id: 0, city: "$_id", population: 1}}, { $sort:{ population: -1 }}, { $skip: 10}, { $limit: 5 }])`
* Quiz answer: there will be zero documents in the result set; if you first limit it to 5 documents, and then skip 10 documents, there will be none left

### Grouping operation (N:1) · Revisiting $first and $last expressions

* `$first` and `$last` are group operators, which allow to get the _first_ or _last value_ in _each group_ as the aggregation pipeline processes documents
* After a _sort stage_, these operators can find the first or last document in _sorted order_ in each group
* If the document set _#{ {A:0, B:23}, {A:0, B:45}, {A:1, B:17}, {A:1, B:68}}_ gets sorted by (A, B), then grouped on A, `$first` would return `B:23` and `B:17`, and `$last` would return `B:45` and `B:68`
* For instance `db.zips.aggregate([{ $sort: { "_id.state": 1, "population": -1}}, { $group: { _id: "$_id.state", city:{ $first: "$_id.city"}, population:{ $first: "$population" }}}])`
* Complete example: we want to find the largest city in every state

    ```javascript
    db.zips.aggregate([
      /* Get the population of every city in every state */
      { $group: { _id:{ state: "$state", city: "$city"}, population:{ $sum: "$pop"}}},
      /* Sort by state, population (note we don't need the dollar operator with $sort) */
      { $sort: { "_id.state": 1, "population": -1}},
      /* Group by state, get the first item in each group */
      { $group: { _id: "$_id.state", city:{ $first: "$_id.city"}, population:{ $first: "$population"}}},
      /* Now sort by state again */
      { $sort: { "_id": 1}}
    ])
    ```

### Unwind and double unwind operations (1:N)

* Allows to _unjoin_ (or _explode_) the data of an array and rejoin it in a way that let us do grouping operations; for instance `db.items.aggregate([{ $unwind: "$attributes"}])`
* Complete example: we want to count the number times that each tag appears in a post (or how many posts were tagged with each tag); therefore, we're going to unwind the tags, and then group by the tag, and count:

    ```javascript
    db.posts.aggregate([
      /* Unwind by tags */
      { "$unwind": "$tags"},
      /* Now group by tags, counting each tag */
      { "$group": { _id: "$tags", count:{ $sum: 1}}},
      /* Sort by popularity */
      { "$sort": { count: -1}},
      /* Show me the top 10 */
      { "$limit": 10},
      /* Change the name of _id to be tag */
      {"$project": { _id: 0, tag: "$_id", count: 1}}
    ])
    ```
* Answer to quiz: `$push` allows to reverse the effect of an `$unwind` (grouping by the rest of the document); another option would be `$addToSet`, depending if the array contained only unique values in the original document
* If there is more than one array in a document, and you want to create a cartesian product of the arrays, you have to _double unwind_
* Complete example:

    ```javascript
    db.inventory.aggregate([
      { $unwind: "$sizes"},
      { $unwind: "$colors"},
      /* Create the color array */
      { $group: { "_id": { name: "$name", size: "$sizes"},
                  "colors":{ $push: "$colors"}}},
      /* Create the size array */
      { $group: { "_id": { "name": "$_id.name", "colors": "$colors"},
                  "sizes":{ $push: "$_id.size"}}},
      /* Reshape for beauty */
      { $project: { _id:0, "name":"$_id.name", "sizes":1, "colors": "$_id.colors"}}
    ])
    ```
* Answer to quiz: can you reverse the effect of a _double unwind_ (two unwinds in a row) with the `$push` operator? Yes, with [two pushes in a row](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_5_Aggregation_Framework/52aa3ec0e2d4232c54a18b29/); or even in a single stage using twice `$addToSet`, if the values were unique

### Mapping from SQL

* Mapping from SQL: `WHERE` → `$match`, `GROUP BY` → `$group`, `HAVING` → `$match`, `SELECT` → `$project`, `ORDER BY` → `$sort`, `LIMIT` → `$limit`, `SUM()` → `$sum`, `COUNT()` → `$sum`, `join` → no direct corresponding operator; `$unwind` allows for similar functionality, but with fields embedded within the document
* Some common examples: see [SQL to Aggregation Mapping Chart](http://docs.mongodb.org/manual/reference/sql-aggregation-comparison/)

### Limitations of the Aggregation Framework

* Resultset limited to **16 MB of memory**
* Can use **max. 10% of the memory** on a machine; use `$match` to do early filtering, if all data is not needed in following stages; similarily, use `$project` to filter out some of the fields
* **Sharding**, that is collections split among multiple Mongo instances (which can be _replica sets_ in turn), with a `mongos` router in front of the shards: aggregation does work on a sharded environment, but after the first `$group` or `$sort` stage, the aggregation has to be brought back to the `mongos`, so that it can gather the results before sending them for the next stage of the pipeline (which needs to see the finished result); so when having a long pipeline, all calculations will wind up to the `mongos` server -- often colocated on the application server, therefore pushing the server resources
* **mapreduce** is an alternative to the Aggregation framework
* **Hadoop** is also an alternative to Aggregation framework; there is a connector for Hadoop in MongoDB, and Hadoop is an implementation of _mapreduce_
