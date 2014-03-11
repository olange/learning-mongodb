# Homework 4.2

What can you infer from the following `explain` output? [Description complète](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_4_Performance/52aa32dfe2d4232c54a18ace/)

## Problème

Suppose you have a collection called tweets whose documents contain information about the created_at time of the tweet and the user's followers_count at the time they issued the tweet. What can you infer from the following explain output?

    > db.tweets.find({"user.followers_count":{$gt:1000}})
               .sort({"created_at" : 1 })
               .limit(10).skip(5000)
               .explain()
    {
            "cursor" : "BtreeCursor created_at_-1 reverse",
            "isMultiKey" : false,
            "n" : 10,
            "nscannedObjects" : 46462,
            "nscanned" : 46462,
            "nscannedObjectsAllPlans" : 49763,
            "nscannedAllPlans" : 49763,
            "scanAndOrder" : false,
            "indexOnly" : false,
            "nYields" : 0,
            "nChunkSkips" : 0,
            "millis" : 205,
            "indexBounds" : {
                    "created_at" : [
                            [
                                    {
                                            "$minElement" : 1
                                    },
                                    {
                                            "$maxElement" : 1
                                    }
                            ]
                    ]
            },
            "server" : "localhost.localdomain:27017"
    }

1. This query performs a collection scan.
2. The query uses an index to determine the order in which to return result documents.
3. The query uses an index to determine which documents match.
4. The query returns 46462 documents.
5. The query visits 46462 documents.
6. The query is a "covered index query".

## Réponse

1. True ⟸ `"nscanned" : 46462`
2. True ⟸ `"cursor" : "BtreeCursor created_at_-1 reverse"`
3. False ⟸ index on field `created_at` was used for sorting, but none was used for searching
4. False ⟸ `"n" : 10` means 10 documents were returned, not 46462
5. True ⟸ `"nscannedObjects" : 46462`
6. False ⟸ `"indexOnly" : false`; it would be true if it was a [covered index query](http://docs.mongodb.org/manual/reference/method/cursor.explain/#explain.indexOnly)
