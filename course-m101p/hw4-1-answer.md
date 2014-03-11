# Homework 4.1

Which of the following queries can utilize an index? [Description complète](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_4_Performance/52aa2f48e2d4232c54a18ac9/)

## Problème

Given a collection with the following indexes (voir [description complète](https://education.mongodb.com/courses/10gen/M101P/2014_February/courseware/Week_4_Performance/52aa2f48e2d4232c54a18ac9/), ou _Préparation_ ci-dessous), which of the following queries can utilize an index?

1. `db.products.find({'brand':"GE"})`
2. `db.products.find({'brand':"GE"}).sort({price:1})`
3. `db.products.find({$and:[{price:{$gt:30}},{price:{$lt:50}}]}).sort({brand:1})`
4. `db.products.find({brand:'GE'}).sort({category:1, brand:-1}).explain()`

## Résolution

Première requête fait un full scan de la collection:

    > db.products.find({'brand':"GE"}).explain()
    {
        "cursor" : "BasicCursor",
        "isMultiKey" : false,
        "n" : 0,
        "nscannedObjects" : 0,
        "nscanned" : 0,
        "nscannedObjectsAllPlans" : 0,
        "nscannedAllPlans" : 0,
        "scanAndOrder" : false,
        "indexOnly" : false,
        "nYields" : 0,
        "nChunkSkips" : 0,
        "millis" : 0,
        "indexBounds" : {
            
        },
        "server" : "QUARK-N.local:27017"
    }

Deuxième requête utilise l'index sur le prix pour le tri (index inversé):

    > db.products.find({'brand':"GE"}).sort({price:1}).explain()
    {
        "cursor" : "BtreeCursor price_-1 reverse",
        "isMultiKey" : false,
        "n" : 0,
        "nscannedObjects" : 2,
        "nscanned" : 2,
        "nscannedObjectsAllPlans" : 4,
        "nscannedAllPlans" : 4,
        "scanAndOrder" : false,
        "indexOnly" : false,
        "nYields" : 0,
        "nChunkSkips" : 0,
        "millis" : 0,
        "indexBounds" : {
            "price" : [
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
        "server" : "QUARK-N.local:27017"
    }

Troisième requête utilise index sur le prix pour la recherche:

    > db.products.find({$and:[{price:{$gt:30}},{price:{$lt:50}}]}).sort({brand:1}).explain()
    {
        "cursor" : "BtreeCursor price_-1",
        "isMultiKey" : false,
        "n" : 0,
        "nscannedObjects" : 0,
        "nscanned" : 0,
        "nscannedObjectsAllPlans" : 0,
        "nscannedAllPlans" : 1,
        "scanAndOrder" : true,
        "indexOnly" : false,
        "nYields" : 0,
        "nChunkSkips" : 0,
        "millis" : 0,
        "indexBounds" : {
            "price" : [
                [
                    50,
                    30
                ]
            ]
        },
        "server" : "QUARK-N.local:27017"
    }

Quatrième requête n'utilise aucun index, ni pour la recherche, ni pour le tri:

    > db.products.find({brand:'GE'}).sort({category:1, brand:-1}).explain()
    {
        "cursor" : "BasicCursor",
        "isMultiKey" : false,
        "n" : 0,
        "nscannedObjects" : 2,
        "nscanned" : 2,
        "nscannedObjectsAllPlans" : 2,
        "nscannedAllPlans" : 2,
        "scanAndOrder" : true,
        "indexOnly" : false,
        "nYields" : 0,
        "nChunkSkips" : 0,
        "millis" : 0,
        "indexBounds" : {
            
        },
        "server" : "QUARK-N.local:27017"
    }

## Réponse

2. `db.products.find({'brand':"GE"}).sort({price:1})` utilise l'index `price_-1` pour le tri (reversed index)
3. `db.products.find({$and:[{price:{$gt:30}},{price:{$lt:50}}]}).sort({brand:1})` utilise l'index `price_-1` pour la recherche

## Préparation

    $ mongo test
    > db.products.insert({ sku: 123, price: 100.00, description: "Refrigerator H-100", category: "Fridge", brand: "Hoover", reviews: [ { author: "Olivier", comment: "Freeeezing"}]})
    > db.products.insert({ sku: 236, price: 120.00, description: "Refrigerator E-100", category: "Fridge", brand: "GE", reviews: [ { author: "Olivier", comment: "Still freeeezing"}]})
    > db.products.ensureIndex({ sku: 1},{ unique: true})
    > db.products.ensureIndex({ price: -1})
    > db.products.ensureIndex({ description: 1})
    > db.products.ensureIndex({ category: 1, brand: 1})
    > db.products.ensureIndex({ "reviews.author": 1})
    > db.products.getIndexes()
    [
        {
            "v" : 1,
            "key" : {
                "_id" : 1
            },
            "ns" : "test.products",
            "name" : "_id_"
        },
        {
            "v" : 1,
            "key" : {
                "sku" : 1
            },
            "unique" : true,
            "ns" : "test.products",
            "name" : "sku_1"
        },
        {
            "v" : 1,
            "key" : {
                "price" : -1
            },
            "ns" : "test.products",
            "name" : "price_-1"
        },
        {
            "v" : 1,
            "key" : {
                "description" : 1
            },
            "ns" : "test.products",
            "name" : "description_1"
        },
        {
            "v" : 1,
            "key" : {
                "category" : 1,
                "brand" : 1
            },
            "ns" : "test.products",
            "name" : "category_1_brand_1"
        },
        {
            "v" : 1,
            "key" : {
                "reviews.author" : 1
            },
            "ns" : "test.products",
            "name" : "reviews.author_1"
        }
    ]
