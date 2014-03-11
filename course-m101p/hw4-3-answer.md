# Homework 4.3

Making the blog fast [Description complète](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_4_Performance/52aa333ae2d4232c54a18ad2/)

## Pièces jointes

* [hw4-3.f798e22df86d.zip](hw4-3.f798e22df86d.zip) application blog mise à dispo par Mongo

## Problème

Your assignment is to make the following blog pages fast:

* The blog home page
* The page that displays blog posts by tag (http://localhost:8082/tag/whatever)
* The page that displays a blog entry by permalink (http://localhost:8082/post/permalink)

By fast, we mean that indexes should be in place to satisfy these queries such that we only need to scan the number of documents we are going to return.

To figure out what queries you need to optimize, you can read the `blog.py` code and see what it does to display those pages. Isolate those queries and use `explain` to explore.

Once you have added the indexes to make those pages fast run the following:

    python validate.py

## Résolution

A quoi ressemblent les données?

    (venv) course-m101p $ mongo
    > use blog
    > db.posts.findOne()
    {
        "_id" : ObjectId("50ab0f8bbcf1bfe2536dc3f8"),
        "body" : "We the People of the United States […]",
        "permalink" : "TqoHkbHyUgLyCKWgPLqm",
        "author" : "machine",
        "title" : "US Constitution",
        "tags" : [ "trade", "fowl", "forecast", "pest", "professor",
            "willow", "rise", "brace", "ink", "road" ],
        "comments" : [
            {   "body" : "Lorem ipsum […]",
                "email" : "LkvwxBUa@LOPSfuBf.com",
                "author" : "Tonia Surace" },
            … ],
        "date" : ISODate("2012-11-20T05:05:15.229Z")
    }

### Blog home page

Situation initiale:

    (venv) course-m101p/hw4-3 $ python validate.py 
    …
    Sorry, executing the query to display the home page is too slow. 
    We should be scanning no more than 10 documents. You scanned 1000
    here is the output from explain
    { … u'millis': 8, u'n': 10, … u'nscanned': 1000 … }
    Sorry, the query to display the blog home page is too slow.

Dans le log de `mongod`, après accès à `http://localhost:8082/`:

    [conn2] query blog.posts query: { $query: {}, $orderby: { date: -1 } } ntoreturn:10 ntoskip:0 nscanned:1000 scanAndOrder:1 keyUpdates:0 locks(micros) W:2213 r:359909 nreturned:10 reslen:309772 360ms

Ajout index inverse sur le champ `date`:

    (venv) course-m101p $ mongo blog
    > db.posts.ensureIndex({ date: -1})

    (venv) course-m101p/hw4-3 $ python validate.py 
    … Home page is super fast. Nice job. …

### Blog entry per permalink

Situation initiale:

    (venv) course-m101p/hw4-3 $ python validate.py 
    …
    Sorry, executing the query to retrieve a post by permalink is too slow 
    We should be scanning no more than 1 documents. You scanned 1000
    here is the output from explain
    { … u'n': 1, u'nscanned': 1000, … }
    Sorry, the query to retrieve a blog post by permalink is too slow.

Dans le log de Mongo, après accès à `http://localhost:8082/post/TLxrBfyxTZjqOKqxgnUP`:

    [conn2] query blog.posts query: { permalink: "TLxrBfyxTZjqOKqxgnUP" } ntoreturn:1 ntoskip:0 nscanned:1000 keyUpdates:0 locks(micros) r:5522 nreturned:1 reslen:27991 5ms

Ajout index sur le champ `permalink`:

    > db.posts.ensureIndex({ permalink: 1}, {unique: true})

    (venv) course-m101p/hw4-3 $python validate.py 
    … Home page is super fast. Nice job. …

### Blog posts per tag

Situation initiale:

    (venv) course-m101p/hw4-3 $python validate.py 
    …
    Sorry, executing the query to retrieve posts by tag is too slow.
    We should be scanning no more than 10 documents. You scanned 690
    here is the output from explain
    { … u'cursor': u'BtreeCursor date_-1', u'n': 10, … u'nscanned': 690, … }
    Sorry, the query to retrieve all posts with a certain tag is too slow

Ajout index sur le champ `tags`

    > db.posts.ensureIndex({ tags: 1})

Première tentative, on a réduit à 13, mais cela ne suffit pas:

    (venv) course-m101p/hw4-3 $python validate.py 
    …
    Sorry, executing the query to retrieve posts by tag is too slow.
    We should be scanning no more than 10 documents. You scanned 13
    here is the output from explain
    { … u'cursor': u'BtreeCursor tags_1',
      u'indexBounds': {u'tags': [[u'sphynx', u'sphynx']]},
      u'indexOnly': False, u'isMultiKey': True, u'millis': 1,
      u'n': 10, … u'nscanned': 13, u'nscannedObjects': 13, … }
    Sorry, the query to retrieve all posts with a certain tag is too slow

Il n'utilise en effet que l'index sur les tags, pour la recherche, mais pas celui sur la date, pour limiter les résultats retournés:

    > db.posts.find({ tags: 'sphynx'}).sort({ date: -1}).limit( 10).explain()
    { … "cursor" : "BtreeCursor tags_1", … "n" : 10, "nscannedObjects" : 13, … }

Combien d'objets?

    > db.posts.count({ tags: 'sphynx'})
    13

Dans le log de Mongo (la requête n'est pas claire):

    [conn5] command blog.$cmd command: { aggregate: "posts", pipeline: [ { $project: { tags: 1 } }, { $unwind: "$tags" }, { $group: { count: { $sum: 1 }, _id: "$tags" } }, { $sort: { count: -1 } }, { $limit: 10 } ] } ntoreturn:1 keyUpdates:0 locks(micros) r:12884 reslen:407 15ms

Code source:

    (blog.py)
    …
    @bottle.route('/tag/<tag>')
    def posts_by_tag(tag="notfound"):
        …
        l = posts.get_posts_by_tag(tag, 10)
        …

    (blogPostDAO.py)
    …
    def get_posts_by_tag(self, tag, num_posts):
        cursor = self.posts.find({'tags':tag}).sort('date', direction=-1).limit(num_posts)
        …

Ajout d'un hint? Ca ne joue pas avec les deux champs:

    > db.posts.find({ tags: 'sphynx'}).sort({ date: -1}).limit( 10)
              .hint({ tags: 1, date: -1}).explain()
    error: { "$err" : "bad hint", "code" : 10113 } 

Que veut dire cette erreur? En essayant la même chose dans le code source:

    (blogPostDAO.py)
    def get_posts_by_tag(self, tag, num_posts):
        cursor = self.posts.find({'tags':tag}).sort('date', direction=-1).limit(num_posts)
        cursor = cursor.hint( [ ("date", pymongo.DESCENDING), ("tags", pymongo.ASCENDING)])

… la validation montre qu'il envisage trois plans, mais n'utilise pas les index sur les tags et la date de façon combinée:

    (venv) course-m101p/hw4-3 $ python validate.py
    …
    Sorry, executing the query to retrieve posts by tag is too slow.
    We should be scanning no more than 10 documents. You scanned 13
    here is the output from explain
    {u'allPlans': [{u'cursor': u'BtreeCursor tags_1', … u'nscannedObjects': 13},
                   {u'cursor': u'BtreeCursor date_-1', … u'nscannedObjects': 13},
                   {u'cursor': u'BasicCursor', … u'nscannedObjects': 13}],

ah! L'erreur obtenue signifie qu'il n'y a pas d'index pour satisfaire le hint. On ajoute l'index combiné et ça joue avec le hint:

    > db.posts.ensureIndex( { tags:1, date: -1})
    > db.posts.find({ tags: 'sphynx'}).sort({ date: -1}).limit( 10)
              .hint({ tags: 1, date: -1}).explain()
    { "cursor" : "BtreeCursor tags_1_date_-1", … "n" : 10, "nscannedObjects" : 10 … }

Ca joue d'ailleurs sans même le hint, l'index combiné était la clé:

    > db.posts.find({ tags: 'sphynx'}).sort({ date: -1}).limit( 10).explain()
    { "cursor" : "BtreeCursor tags_1_date_-1", … "n" : 10, "nscannedObjects" : 10 … }

## Réponse

    (venv) course-m101p/hw4-3 $ python validate.py
    Welcome to the HW 4.3 Checker. My job is to make sure you added the indexes
    that make the blog fast in the following three situations
        When showing the home page
        When fetching a particular post
        When showing all posts for a particular tag
    Data looks like it is properly loaded into the posts collection
    Home page is super fast. Nice job.

    Blog retrieval by permalink is super fast. Nice job.

    Blog retrieval by tag is super fast. Nice job.

    Tests Passed for HW 4.3. Your HW 4.3 validation code is 893jfns29f728fn29f20f2

    --> 893jfns29f728fn29f20f2

## Préparation

Chargement des données

    (venv) course-m101p $ mongo
    > use blog
    > db.posts.drop()
    > exit

    (venv) course-m101p $ mongoimport -d blog -c posts < hw4-3/posts.json
    connected to: 127.0.0.1
    Tue Mar  4 18:36:12.354             500 166/second
    Tue Mar  4 18:36:15.268             1000    166/second
    Tue Mar  4 18:36:15.268 check 9 1000
    Tue Mar  4 18:36:15.268 imported 1000 objects

Serveur Mongo en mode _profiling_

    (venv) course-m101p $ tail -f /usr/local/var/log/mongodb/mongo.log &
    …
    (venv) course-m101p $ mongod --dbpath data/db --profile 1 --slowms 2
    …

Application

    (venv) course-m101p $ python blog.py
